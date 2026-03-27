# 🛡️ AI-Native DLP Agent 

[English](#english) | [中文](#chinese)

<a name="chinese"></a>
## 📖 项目简介
这是一个基于 **生成式 AI (LLM)** 的数据泄露防护 (DLP) 工具。不同于传统的基于规则或正则表达式的检测，本项目利用大模型的语义理解能力，实现对敏感数据的 **“识别-判定-重写”** 全流程自动化处理。

### ✨ 核心功能
- **全格式支持**：基于 `unstructured` 库，支持 PDF, Docx, TXT, PPTX 等多种文件解析。
- **语义级检测**：摒弃死板的正则，通过 AI 识别隐藏在上下文中的敏感意图。
- **智能执行**：
  - **Block (阻断)**：生成人性化的安全解释。
  - **Mask (脱敏)**：语义无损重写，使用占位符替换敏感实体，保持文档可读性。
- **模型中立**：支持任何兼容 OpenAI 协议的 API（如 DeepSeek, OpenAI, Ollama 本地模型）。

## 🚀 快速开始

### 1. 环境配置
```bash
# 克隆项目
git clone [https://github.com/你的用户名/AI-DLP-Agent.git](https://github.com/你的用户名/AI-DLP-Agent.git)
cd AI-DLP-Agent

# 创建并激活虚拟环境
python -m venv .venv
source .venv/bin/activate  # Windows 使用 .venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
