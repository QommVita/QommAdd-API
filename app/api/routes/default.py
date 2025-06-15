"""Module that defines the main API routes using FastAPI/"""
from fastapi import FastAPI
from app.api.routes import events

app = FastAPI(title="My Python API", version="0.1.0")
app.include_router(events.router)

@app.get("/")
def read_root():
    """
    Main endpoint that returns a welcome message.
    
    Returns:
        dict: JSON welcome message with structure:
            {"message": "Welcome to my API"}
    """
    return {"message": "Welcome to my API"}