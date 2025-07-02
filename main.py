from fastapi import FastAPI, Request
import datetime

app = FastAPI()

# In-memory log to track agent communication
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

@app.get("/")
async def root():
    return {"message": "🚀 AI Agent SaaS is running on Render!"}

@app.post("/ceo")
async def ceo_agent(request: Request):
    body = await request.json()
    vision = body.get("vision")
    log_interaction("User", "CEOAgent", vision)
    return {"agent": "CEOAgent", "message": f"Vision received: {vision}"}

@app.post("/cmo")
async def cmo_agent(request: Request):
    body = await request.json()
    vision = body.get("vision")
    log_interaction("CEOAgent", "CMOAgent", vision)
    return {"agent": "CMOAgent", "message": f"Campaign strategy based on: {vision}"}

@app.post("/cro")
async def cro_agent(request: Request):
    body = await request.json()
    vision = body.get("vision")
    log_interaction("CEOAgent", "CROAgent", vision)
    return {"agent": "CROAgent", "message": f"Revenue offer aligned with: {vision}"}

@app.post("/creative")
async def creative_agent(request: Request):
    body = await request.json()
    prompt = body.get("strategy")
    log_interaction("CMOAgent", "CreativeAgent", prompt)
    return {"agent": "CreativeAgent", "message": f"Creative assets developed for: {prompt}"}

@app.post("/paid-media")
async def paid_media_agent(request: Request):
    body = await request.json()
    prompt = body.get("creative")
    log_interaction("CreativeAgent", "PaidMediaAgent", prompt)
    return {
        "agent": "PaidMediaAgent",
        "message": f"Paid media strategy created for: {prompt}"
    }

@app.post("/web-ux")
async def web_ux_agent(request: Request):
    body = await request.json()
    prompt = body.get("mediaPlan")
    log_interaction("PaidMediaAgent", "WebUXAgent", prompt)
    return {
        "agent": "WebUXAgent",
        "message": f"Website UX plan created based on: {prompt}"
    }

@app.post("/scraper")
async def scraper_agent(request: Request):
    body = await request.json()
    target = body.get("target")
    log_interaction("WebUXAgent", "ScraperAgent", target)
    return {
        "agent": "ScraperAgent",
        "message": f"Scraped 500 contacts from {target}"
    }

@app.post("/crm")
async def crm_agent(request: Request):
    body = await request.json()
    leads = body.get("leads", [])
    log_interaction("ScrapingAgent", "CRMAgent", str(leads))
    return {"agent": "CRMAgent", "message": f"Logged {len(leads)} leads."}

@app.post("/sdr")
async def sdr_agent(request: Request):
    body = await request.json()
    leads = body.get("leads", [])
    log_interaction("CRMAgent", "SDRAgent", str(leads))
    return {"agent": "SDRAgent", "message": f"Engaging {len(leads)} leads."}

@app.post("/closer")
async def closer_agent(request: Request):
    body = await request.json()
    contacts = body.get("contacts", [])
    log_interaction("SDRAgent", "CloserAgent", str(contacts))
    return {"agent": "CloserAgent", "message": f"Closed deals with {len(contacts)} contacts."}

@app.post("/coo")
async def coo_agent(request: Request):
    body = await request.json()
    clients = body.get("clients", [])
    log_interaction("CloserAgent", "COOAgent", str(clients))
    return {"agent": "COOAgent", "message": f"Service delivery started for {len(clients)} clients."}

@app.post("/measure")
async def measurement_agent(request: Request):
    body = await request.json()
    campaign = body.get("campaign")
    log_interaction("COOAgent", "CMO/CROAgent", campaign)
    return {"agent": "CMO/CROAgent", "message": f"Measured performance for: {campaign}"}

@app.get("/log")
async def get_log():
    return {"log": agent_log}
