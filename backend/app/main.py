from fastapi import FastAPI

app = FastAPI(title="Cloud Incident Automation Platform")

@app.get("/health")
def health_check():
    return {"status": "ok"}
