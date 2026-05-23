from fastapi import FastAPI

app = FastAPI(
    title="SentinelX API",
    description="AI-Powered Cyber Threat Intelligence System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "SentinelX Backend Running Successfully"
    }