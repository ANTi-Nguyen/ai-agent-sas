# AI Agent SaaS Core Framework (Fully Dynamic, Collaborative 24/7 Loop)

from fastapi import FastAPI, Request
import datetime

app = FastAPI()

agent_log = []

def log_interaction(sender, recipient, message):
    timestamp = datetime.datetime.utcnow().isoformat()
    entry = {
        "timestamp": timestamp,
        "from": sender,
        "to": recipient,
        "message": message
    }
    agent_log.append(entry)
    return entry

@app.post("/ceo")
async def ceo_agent(request: Request):
    body = await request.json()
    vision = body.get("vision")
    log_interaction("User", "CEOAgent", vision)
    return {"agent": "CEOAgent", "message": vision}

@app.post("/cmo")
async def cmo_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CEOAgent", "CMOAgent", prompt)
    return {"agent": "CMOAgent", "message": prompt}

@app.post("/creative")
async def creative_agent(request: Request):
    body = await request.json()
    task = body.get("prompt")
    log_interaction("CMOAgent", "CreativeAgent", task)
    return {"agent": "CreativeAgent", "message": f"Creative assets developed for: {task}"}

@app.post("/media")
async def media_agent(request: Request):
    body = await request.json()
    task = body.get("prompt")
    log_interaction("CMOAgent", "PaidMediaAgent", task)
    return {"agent": "PaidMediaAgent", "message": f"Ad campaigns launched for: {task}"}

@app.post("/webux")
async def webux_agent(request: Request):
    body = await request.json()
    task = body.get("prompt")
    log_interaction("CMOAgent", "WebUXAgent", task)
    return {"agent": "WebUXAgent", "message": f"Landing pages and funnels built for: {task}"}

@app.post("/scraper")
async def scraper_agent(request: Request):
    body = await request.json()
    task = body.get("prompt")
    log_interaction("CMOAgent", "ScraperAgent", task)
    return {"agent": "ScraperAgent", "message": f"Leads scraped for: {task}"}

@app.post("/crm")
async def crm_agent(request: Request):
    body = await request.json()
    contacts = body.get("prompt")
    log_interaction("ScraperAgent", "CRMAgent", contacts)
    return {"agent": "CRMAgent", "message": f"CRM updated with: {contacts}"}

@app.post("/sdr")
async def sdr_agent(request: Request):
    body = await request.json()
    leads = body.get("prompt")
    log_interaction("CRMAgent", "SDRAgent", leads)
    return {"agent": "SDRAgent", "message": f"Engaged leads: {leads}"}

@app.post("/closer")
async def closer_agent(request: Request):
    body = await request.json()
    leads = body.get("prompt")
    log_interaction("SDRAgent", "CloserAgent", leads)
    return {"agent": "CloserAgent", "message": f"Converted leads: {leads}"}

@app.post("/coo")
async def coo_agent(request: Request):
    body = await request.json()
    deliverables = body.get("prompt")
    log_interaction("CloserAgent", "COOAgent", deliverables)
    return {"agent": "COOAgent", "message": f"Service delivery initiated for: {deliverables}"}

@app.post("/cmo-feedback")
async def cmo_feedback_agent(request: Request):
    body = await request.json()
    feedback = body.get("prompt")
    log_interaction("COOAgent", "CMOFeedbackAgent", feedback)
    decision = f"Based on agent collaboration, next move: Scale campaign around '{feedback}'"
    return {"agent": "CMOFeedbackAgent", "decision": decision}

@app.get("/log")
async def get_log():
    return {"log": agent_log}
