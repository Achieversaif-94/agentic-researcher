    **************
# 🕵️ Agentic Researcher — Autonomous AI Research Team

A multi-agent AI system that takes a research topic, autonomously searches the live web, scrapes the top articles, and generates a fully cited, structured markdown report. 

Unlike standard "Chat with PDF" or single-prompt LLMs, this system uses an Agentic Workflow where a **Researcher Agent** and a **Writer Agent** collaborate sequentially to gather facts and draft a flawless report.

**🔴 Live Web Demo:** [https://agenticresearcher.streamlit.app/]

## 🏗️ Architecture

```text
User Input (Topic)
   ↓
[CrewAI Orchestrator]
   ↓
[🕵️ Senior Research Analyst Agent]
   ├── Tool: DuckDuckGo Web Search (Free, no API key)
   ├── Action: Searches web, extracts facts, titles, and URLs
   ↓
[✍️ Tech Content Writer Agent]
   ├── Action: Synthesizes facts into a structured report
   └── Rule: Strict citation enforcement (no hallucinated URLs)
   ↓
Streamlit UI (Markdown display + Download as .md)
🧠 How It Works
Most AI apps are just a single LLM call. This project uses Agentic Orchestration via CrewAI:

The Researcher Agent is equipped with a custom WebSearchTool built on top of DuckDuckGo. It actively queries the web for the latest articles and extracts raw text snippets and URLs.

The Writer Agent receives the Researcher's notes. It is strictly prompted to generate a report with an Introduction, Key Findings, and a Conclusion, using only the URLs provided by the Researcher.

🛠️ Tech Stack
Agent Framework: CrewAI (for orchestrating roles, tasks, and tools)

LLM Engine: Groq (Model: openai/gpt-oss-120b for ultra-fast, zero-cost inference)

Search Tool: DuckDuckGo Search (ddgs) (100% free, requires no API keys)

UI: Streamlit

Deployment: Streamlit Community Cloud

⚠️ Limitations & Engineering Caveats
Context Window vs. Snippets: The agent only reads the text snippets provided by the search engine, not the full articles. This prevents token overflow but may miss deep context.

DuckDuckGo Rate Limits: Because the search tool scrapes DuckDuckGo directly, rapid-fire queries may result in temporary rate limits.

Groq API Guardrails (Solved): During development, we encountered a cache_breakpoint error because CrewAI automatically injects Anthropic-specific caching headers. This was resolved via a custom Python monkey-patch in agents_and_tasks.py to strip the headers for Groq compatibility.

Prompt Dependency: The quality of the report relies heavily on the search query the Researcher generates. Broad or ambiguous topics may retrieve unexpected news snippets.

🚀 Run Locally
Clone the repo: git clone https://github.com/Achieversaif-94/agentic-researcher.git

Create a virtual environment: python -m venv venv

Activate it: .\venv\Scripts\Activate.ps1 (Windows) or source venv/bin/activate (Mac/Linux)

Install dependencies: pip install -r requirements.txt

Create a .env file and add your Groq API Key: GROQ_API_KEY=gsk_your_key_here

Run the CLI: python src/crew.py "The future of quantum computing"

Run the UI: streamlit run app.py
