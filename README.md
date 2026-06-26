# Agentic Deep Researcher

> **An MCP-powered multi-agent AI research assistant** that performs deep web research using intelligent agent collaboration, powered by **CrewAI**, **LinkUp**, and **DeepSeek R1**, with an interactive **Streamlit** interface.

---

## 🚀 Overview

Agentic Deep Researcher is an AI-powered research assistant designed to automate comprehensive web research through a team of specialized AI agents.

Instead of relying on a single LLM response, the application uses a **multi-agent architecture** where agents collaborate to search, analyze, verify, and synthesize information into high-quality research results.

The agents are orchestrated using **CrewAI**, while **LinkUp** provides real-time web search capabilities. The application is wrapped in a clean and interactive **Streamlit** interface for an intuitive user experience.

---

## ✨ Features

* 🔍 Deep web research using **LinkUp**
* 🤖 Multi-agent orchestration with **CrewAI**
* 🧠 Powered by **DeepSeek R1**
* ⚡ MCP (Model Context Protocol) powered architecture
* 🌐 Real-time internet search
* 📑 Comprehensive research reports
* 🎯 Interactive Streamlit UI
* 🛠 Modular and extensible design

---

## 🏗 Tech Stack

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| **CrewAI**      | Multi-agent orchestration |
| **LinkUp**      | Web search tool           |
| **DeepSeek R1** | Large Language Model      |
| **Streamlit**   | User Interface            |
| **Python**      | Backend development       |
| **MCP**         | Model Context Protocol    |

---

## 📂 Project Structure

```bash
Agentic-Deep-Researcher/
│
├── app.py                 # Streamlit application
├── agents/                # AI agent definitions
├── tasks/                 # Research workflows
├── tools/                 # LinkUp search tools
├── config/                # Configuration files
├── requirements.txt
├── pyproject.toml
├── uv.lock
└── README.md
```

> *Project structure may vary depending on your implementation.*

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/agentic-deep-researcher.git
```

Navigate to the project directory:

```bash
cd agentic-deep-researcher
```

Install dependencies:

```bash
uv sync
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## 🧠 How It Works

1. User submits a research query.
2. CrewAI orchestrates multiple specialized agents.
3. LinkUp performs deep web searches.
4. DeepSeek R1 analyzes and synthesizes the gathered information.
5. Streamlit presents the research results in an interactive interface.

---

## 📌 Requirements

* Python 3.11+
* uv
* Streamlit
* CrewAI
* LinkUp API Key
* DeepSeek API Access

---

## 🚀 Future Improvements

* PDF report generation
* Citation support
* Research history
* Multi-document analysis
* Export to Markdown/PDF
* Additional search providers
* Custom agent workflows

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub to support its development.
