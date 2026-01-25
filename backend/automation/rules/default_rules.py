def apply_rules(incident: dict) -> dict:
    incident_type = incident.get("type")
    severity = incident.get("severity")

    if incident_type == "CPU_HIGH" and severity >= 3:
        return {
            "action": "SCALE_UP",
            "reason": "High CPU usage detected"
        }

    if incident_type == "SERVICE_DOWN":
        return {
            "action": "RESTART_SERVICE",
            "reason": "Service unavailable"
        }

    return {
        "action": "NO_ACTION",
        "reason": "No matching rule found"
    }
