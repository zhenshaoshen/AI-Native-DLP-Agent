import streamlit as st
import requests
import json
from unstructured.partition.auto import partition
import os

# --- 1. 配置区 (填入你的 API 信息) / Your API Configuration---
API_KEY = "Replace your API Key/ 配置API KEY"
API_URL = "Make your API URL / 配置API URL"
MODEL_NAME = "Choose your Model / 选择模型"

def call_ai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}]
        # 注意：这里我们去掉了强制 JSON 格式的限制，让它更通用 / No compulsory JSON type for smooth
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        res_json = response.json()
        
        # 获取 AI 的回复原文 / Get Respond
        ans = res_json['choices'][0]['message']['content']
        
        # --- 核心修复逻辑 ---
        # 尝试看看是不是 JSON，如果是就转成字典，如果不是就直接返回字符串 / If respond is not Json, turn to Dictionary. Or go string
        try:
            return json.loads(ans)
        except:
            return ans 
            
    except Exception as e:
        return f"请求出错了 / error: {str(e)}}"
# --- 2. 网页界面设计 Web UI---
st.set_page_config(page_title="AI 数据泄露防护系统/ DLP", layout="wide")

st.title("🛡️ 智能数据安全处理 Agent")
st.markdown("上传文件后，AI 将自动进行：**内容解析 -> 风险判定 -> 智能脱敏**")

# 创建左右两栏
col1, col2 = st.columns(2)

with col1:
    st.header("文件上传/ upload")
    uploaded_file = st.file_uploader("选择要上传的文件/choose upload file", type=["pdf", "docx", "txt", "pptx"])

# --- 3. 核心处理逻辑 main---
if uploaded_file is not None:
    # 将上传的文件保存到本地临时路径，方便解析
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with col1:
        with st.spinner("AI 正在深度审计中..."):
            # A. 解析内容
            elements = partition(filename=uploaded_file.name)
            raw_text = "\n\n".join([str(el) for el in elements])
            
            # B. 扫描敏感项
            scanner_prompt = f"以JSON格式提取text中的敏感项清单(entities:[])：\n{raw_text[:2000]}" # 限制长度防止超限
            entities = call_ai(scanner_prompt)
            
            # C. 风险决策
            judge_prompt = f"基于这些实体：{entities}，判定风险(High/Low)和动作(Block/Mask/Pass)，返回JSON：{{'action': '...', 'reason': '...'}}"
            decision = call_ai(judge_prompt)
            
            st.success("审计完成！")
            st.json(decision) # 显示 AI 的决策过程

    with col2:
        st.header("处理结果")
        action = decision.get("action")
        
        if action == "Block":
            st.error("🚫 文件外发被阻断")
            exec_prompt = f"生成一段正式的安全拦截通知，说明原因：{decision['reason']}"
            block_msg = call_ai(exec_prompt)
            # 这里的 block_msg 现在是纯文字了，直接显示即可
            st.warning(block_msg)
            
        elif action == "Mask":
            st.info("⚠️ 内容已自动脱敏")
            exec_prompt = f"重写这段话，将敏感项替换为[机密处理]，保持语义通顺：\n{raw_text[:2000]}"
            sanitized_text = call_ai(exec_prompt)
            # 直接显示 AI 重写后的文字
            st.text_area("脱敏后的文本内容：", value=str(sanitized_text), height=400)
            
        else:
            st.success("✅ 检查通过，无敏感信息")
            st.text_area("原文内容：", value=raw_text, height=400)

    # 清理生成的临时文件
    os.remove(uploaded_file.name)
