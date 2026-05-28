from fastapi import FastAPI

from app.database import engine, Base

# Import models
from app.models.user_model import User

# Import routes
from app.routes.auth_route import router as auth_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SentinelX API",
    description="AI-Powered Cyber Threat Intelligence System",
    version="1.0.0"
)

# Register routes
app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "SentinelX Backend Running Successfully"
    }