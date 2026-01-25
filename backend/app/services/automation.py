from .classifier import SeverityLevel

def decide_action(severity: SeverityLevel) -> str:
    if severity == SeverityLevel.CRITICAL:
        return "AUTO_REMEDIATE"
    elif severity == SeverityLevel.HIGH:
        return "ALERT_ON_CALL"
    elif severity == SeverityLevel.MEDIUM:
        return "CREATE_TICKET"
    else:
        return "LOG_ONLY"
