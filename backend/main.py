"""
AI-Based Accident Detection System - Backend
Main FastAPI Application Entry Point

Author: Your Name
Date: January 2026
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from database import init_database
from routes import router
import os

# Initialize FastAPI app
app = FastAPI(
    title="AI Accident Detection System API",
    description="Backend API for real-time accident detection and emergency alerts",
    version="1.0.0"
)

# Configure CORS - Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api", tags=["Accident Detection"])

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    """Initialize database tables when server starts"""
    init_database()
    print("✅ Database initialized successfully")
    print("✅ Server is ready to accept requests")

# Root endpoint
@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "message": "AI Accident Detection System API is running",
        "version": "1.0.0"
    }

# Run server
if __name__ == "__main__":
    print("🚀 Starting AI Accident Detection System Backend...")
    print("📍 Server started")
    print("📚 API Documentation available at /docs")

    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=False  # Auto-reload on code changes (disable in production)
    )