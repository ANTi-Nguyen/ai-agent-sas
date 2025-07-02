# AI Agent SaaS Core Framework (Fully Dynamic, Collaborative 24/7 Loop)
from fastapi import FastAPI, Request
import datetime

app = FastAPI()

# Agent communication log
agent_log = []

# Logging function
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
    return {"agent": "CMOAgent", "message": f"CMO received: '{prompt}' and is assigning tasks to all agents."}

@app.post("/cro")
async def cro_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CMOAgent", "CROAgent", prompt)
    return {"agent": "CROAgent", "message": f"CRO Strategy aligned for: '{prompt}'."}

@app.post("/market-research")
async def market_research_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CMOAgent", "MarketResearchAgent", prompt)
    return {"agent": "MarketResearchAgent", "message": f"Market trends and insights gathered for: '{prompt}'."}

@app.post("/analytics")
async def analytics_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CMOAgent", "AnalyticsAgent", prompt)
    return {"agent": "AnalyticsAgent", "message": f"Analytics processed for: '{prompt}'."}

@app.post("/creative")
async def creative_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CMOAgent", "CreativeAgent", prompt)
    return {"agent": "CreativeAgent", "message": f"Creative assets and strategy created for: '{prompt}'."}

@app.post("/paid-media")
async def paid_media_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CMOAgent", "PaidMediaAgent", prompt)
    return {"agent": "PaidMediaAgent", "message": f"Paid media campaigns developed for: '{prompt}'."}

@app.post("/sales")
async def sales_director_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CMOAgent", "DirectorOfSalesAgent", prompt)
    return {"agent": "DirectorOfSalesAgent", "message": f"Sales team aligned for: '{prompt}'."}

@app.post("/crm")
async def crm_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CMOAgent", "CRMAgent", prompt)
    return {"agent": "CRMAgent", "message": f"CRM updated and customer flow optimized for: '{prompt}'."}

@app.post("/scraper")
async def scraper_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CMOAgent", "ScraperAgent", prompt)
    return {"agent": "ScraperAgent", "message": f"Scraped and enriched lead data for: '{prompt}'."}

@app.post("/video")
async def video_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CMOAgent", "VideoAgent", prompt)
    return {"agent": "VideoAgent", "message": f"Video content and scripts generated for: '{prompt}'."}

@app.post("/scheduler")
async def scheduler_agent(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    log_interaction("CMOAgent", "SchedulerAgent", prompt)
    final_output = f"Content scheduled strategically for: '{prompt}'."
    log_interaction("SchedulerAgent", "CMOAgent", final_output)
    return {"agent": "SchedulerAgent", "message": final_output}

@app.get("/log")
async def get_log():
    return {"log": agent_log}
