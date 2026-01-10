from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.visa import router as visa_router

app = FastAPI()

# Enable CORS for all origins (for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change '*' to your frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(visa_router)
