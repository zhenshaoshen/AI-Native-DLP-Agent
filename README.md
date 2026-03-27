# 🛡️ AI-Native DLP Agent 

- [English (Default)](./docs/en/README.md)
- [简体中文](./docs/zh/README.md)

---



```markdown
# 🛡️ AI-Native DLP Agent: Intelligent Data Protection

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Introduction

An next-generation **Data Loss Prevention (DLP)** system built entirely on **Generative AI**.

Unlike traditional DLP tools that rely on static Regular Expressions (Regex) or keyword matching, this project leverages the semantic power of Large Language Models (LLMs) to identify complex leak intents, unstructured business secrets, and provide intelligent "Generative Redaction."

## ✨ Key Features

* **Semantic-Aware Detection (No-Regex)**: Moves beyond rigid patterns to identify hidden sensitive info in context, such as proprietary logic, unreleased plans, or obfuscated contact details.
* **Multi-format Support**: Automatic parsing and analysis for PDF, Word, TXT, PPTX, and more.
* **Triple-Agent Workflow**:
    1.  **Scanner Agent**: Extracts all potential sensitive entities.
    2.  **Judge Agent**: Performs risk assessment (High/Low) and provides disposal advice based on context.
    3.  **Executor Agent**: Rewrites content (Mask) or generates security alerts (Block).
* **Generative Redaction**: Instead of simple masking (e.g., `[***]`), the AI rewrites the content to be "safe" while maintaining natural language flow and business utility.
* **Model Agnostic**: Fully compatible with any OpenAI-compliant API (OpenAI, DeepSeek, or local Ollama models).

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/AI-DLP-Agent.git](https://github.com/your-username/AI-DLP-Agent.git)
cd AI-DLP-Agent

###2. Set Up Virtual Environment
```Bash
python -m venv .venv
# Activate (Windows)
.venv\Scripts\activate
# Activate (macOS/Linux)
source .venv/bin/activate

pip install -r requirements.txt

### 3. Configuration
Rename .env.example to .env.

Fill in your API Key and endpoint in .env:


AI_API_KEY=your_key_here
AI_API_URL=[https://api.openai.com/v1/chat/completions](https://api.openai.com/v1/chat/completions)
AI_MODEL_NAME=gpt-4o

### 4. Launch the Web UI
```Bash
streamlit run app.py


### 📂 Project Structure

├── app.py              # Streamlit Entry point
├── core/               # Core Agent logic
├── .env.example        # Config template
├── requirements.txt    # Dependency list
└── .gitignore          # Git ignore rules
