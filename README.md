# AI Agent SaaS

This is an AI-powered SaaS system using FastAPI that simulates a full marketing and sales organization — from CEO vision to CMO/CRO decision-making.

## 🚀 Features
- FastAPI endpoints for each executive and operational role
- Logs all agent-to-agent communication
- Ready for integration with n8n or automation platforms

## 🧠 Workflow Overview

1. CEO sets vision
2. CMO + CRO align strategy
3. Creative, Paid Media, Web UX execute
4. Scraper finds leads → CRM logs them
5. SDRs engage → Closers convert
6. COO fulfills
7. CMO/CRO measure & iterate

## 🛠 How to Run

```bash
uvicorn main:app --reload
```

## 📦 Deployment (Render)

Create a new web service with this repo and set the start command:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```
