# Claude AI Enterprise Bot

> An intelligent enterprise assistant built on the **Claude API** that answers questions from your own documents — PDFs, Word files, CSVs — in plain English.

## The Problem
A company had 200+ internal policy documents that nobody actually read. Employees wasted time asking HR basic questions. I built this bot so they could just ask questions and get answers from the actual documents.

## Features
- 📄 Upload PDFs, DOCX, CSV — bot reads and indexes them
- 💬 Ask questions in plain English, get precise answers with source references
- 🧠 Multi-turn conversation with memory (context compression for long sessions)
- 🎫 Auto ticket routing based on query classification
- 📊 Admin dashboard: usage stats, cost tracking, conversation logs

## Stack
```
Claude API (Anthropic) | FastAPI | React | PostgreSQL | LangChain | Redis
```

## Quick Start
```bash
git clone https://github.com/shebinsillikkal/claude-ai-enterprise-bot
cd claude-ai-enterprise-bot
pip install -r requirements.txt
cp .env.example .env   # Add your ANTHROPIC_API_KEY
uvicorn app.main:app --reload
```

## Contact
Built by **Shebin S Illikkal** — [Shebinsillikkl@gmail.com](mailto:Shebinsillikkl@gmail.com)
