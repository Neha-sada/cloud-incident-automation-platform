from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from backend.app.services.classifier import classify_incident
from backend.app.services.automation import decide_action
from backend.automation.engine import process_incident



app = FastAPI(title="Cloud Incident Automation Platform")

# ---- Health Check ----
@app.get("/health")
def health():
    return {"status": "ok"}

# ---- Incident Model ----
class IncidentEvent(BaseModel):
    service: str
    severity: str
    message: str
    timestamp: Optional[datetime] = None

# Temporary in-memory incident store
incidents_db = []

# ---- Incident Ingestion API ----
@app.post("/incidents")
def ingest_incident(event: IncidentEvent):
    if event.timestamp is None:
        event.timestamp = datetime.utcnow()

    severity_level = classify_incident(event.severity)
    action = decide_action(severity_level)

    record = {
        "incident": event,
        "classified_severity": severity_level,
        "action": action
    }

    incidents_db.append(record)

    return {
        "status": "processed",
        "action": action,
        "incident": event
    }

@app.post("/automate")
def automate_incident(incident: dict):
    return process_incident(incident)
