from enum import Enum

class SeverityLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

def classify_incident(severity: str) -> SeverityLevel:
    severity = severity.lower()

    if severity in ["critical", "sev1"]:
        return SeverityLevel.CRITICAL
    elif severity in ["high", "sev2"]:
        return SeverityLevel.HIGH
    elif severity in ["medium", "sev3"]:
        return SeverityLevel.MEDIUM
    else:
        return SeverityLevel.LOW
