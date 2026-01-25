from backend.automation.rules.default_rules import apply_rules

def process_incident(incident: dict) -> dict:
    result = apply_rules(incident)
    return {
        "incident_id": incident.get("id"),
        "decision": result
    }
