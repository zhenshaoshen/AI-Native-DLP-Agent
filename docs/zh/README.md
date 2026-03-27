# 🛡️ AI-Native DLP Agent: 智能数据泄露防护助手

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📖 项目简介

这是一个完全基于 **生成式 AI (Generative AI)** 构建的数据泄露防护 (DLP) 工具。

传统的 DLP 依赖正则表达式（Regex），难以识别复杂的语义风险。本项目利用大语言模型 (LLM) 的推理能力，实现了从“规则匹配”到“意图识别”的跨越，能够像安全专家一样“读懂”文档，并智能地对敏感内容进行重写或拦截。

### ✨ 核心亮点

- **语义级安全审计**: 不再纠结于手机号格式，AI 能识别隐藏在上下文中的商业机密、代码密钥和违规意图。
- **不限格式的文件解析**: 集成 `unstructured` 库，支持 PDF, Word, TXT, PPTX 等多种格式的一键导入。
- **生成式智能脱敏**: AI 不仅仅是“打码”，它会根据上下文重新生成“安全”的替代文本，确保文档在脱敏后依然逻辑通顺、可读性强。
- **高度灵活的模型适配**: 兼容所有 OpenAI 协议的 API（如 GPT-4, DeepSeek, LongCat），也支持通过 Ollama 纯本地运行。

---

## 🛠️ 技术架构

项目采用模块化 Agent 设计：

1. **识别体 (Scanner)**: 提取文本中的潜在敏感项。
2. **决策体 (Judge)**: 判定风险等级 (High/Low) 并给出处理动作。
3. **执行体 (Executor)**: 进行生成式脱敏或发布拦截警告。

---

## 🚀 快速开始

### 1. 环境准备

建议在 Python 虚拟环境中运行：

```bash
python -m venv .venv
# 激活环境 (Windows)
.venv\Scripts\activate
# 激活环境 (macOS/Linux)
source .venv/bin/activate

pip install -r requirements.txt
```





## 2. 配置虚拟环境

```bash
python -m venv .venv
# 激活环境 (Windows)
.venv\Scripts\activate
# 激活环境 (macOS/Linux)
source .venv/bin/activate

pip install -r requirements.txt
```

## 3. API 与环境配置

1. 将项目根目录下的 `.env.example` 重命名为 `.env`。
2. 在 `.env` 中填写你的 API Key 和模型地址：



```bash
AI_API_KEY= 你的API Key
AI_API_URL= 你的API格式/接口类型
AI_MODEL_NAME= 模型名称
```

## 4. 启动 Web 界面

```bash
streamlit run app.py
```

## 📂 项目结构

```
├── app.py              # Streamlit 网页端入口
├── core/               # 核心逻辑模块
├── .env.example        # 配置模板
├── requirements.txt    # 依赖清单
└── .gitignore          # 忽略私密信息与缓存
```
