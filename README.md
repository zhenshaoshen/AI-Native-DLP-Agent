# 🛡️ AI-Native DLP Agent 

- [English (Default)](./docs/en/README.md)
- [简体中文](./docs/zh/README.md)

Semantic-Aware Data Protection & Intelligent Redaction Powered by LLMs
AI-Native DLP Agent is a next-generation Data Loss Prevention (DLP) system that moves beyond the limitations of static patterns and Regular Expressions (Regex). By leveraging the reasoning capabilities of Large Language Models (LLMs), it understands the context and intent behind data, enabling precise identification of sensitive information and business secrets that traditional tools often miss.

🚀 Key Features
🧠 1. Semantic-Aware Identification (Zero-Regex)
Unlike traditional DLP tools that rely on rigid patterns, this agent uses LLMs to understand why information is sensitive. It can detect obfuscated secrets, proprietary logic, and "leaky" intents that don't follow a standard format like a credit card number.

🎭 2. Generative Redaction (Smart Masking)
Instead of simply "blacking out" text with [***], the Executor Agent performs generative rewriting. It produces a "safe" version of the document that maintains grammatical flow and business utility while ensuring all sensitive entities are replaced with consistent, non-identifiable pseudonyms.

🤖 3. Triple-Agent Workflow
The system orchestrates three specialized sub-agents to create a "Detect-Decide-Execute" loop:

The Scanner: Performs a deep semantic scan to extract potential sensitive entities.

The Judge: Assesses risk levels (High/Medium/Low) based on the context and predefined security policies.

The Executor: Automatically applies the appropriate action—either blocking the output or intelligently masking the content.

📂 4. Universal Document Parsing
Built-in support for multiple file formats, including PDF, DOCX, PPTX, and TXT, ensuring a seamless workflow regardless of the data source.

🔌 5. Model Agnostic & Privacy-First
Fully compatible with any OpenAI-compliant API. Whether you are using Cloud APIs (GPT, DeepSeek ……) or Local Models via Ollama, your data security is in your hands.

🛠️ Tech Stack
Frontend: Streamlit (Python-based Web UI)

Orchestration: Python

Parsing: Unstructured.io

Inference: OpenAI-Compatible APIs / Ollama

Why use this?
Traditional DLP is a headache for developers and security teams because it generates too many false positives and breaks document readability. AI-Native DLP Agent fixes this by treating data security as a language task, making it smarter, more flexible, and truly context-aware.
