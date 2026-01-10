# app/routes/visa.py

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.services.ai_service import process_visa_request

router = APIRouter(
    prefix="/visa",
    tags=["Visa AI"]
)

@router.post("/ask")
async def ask_visa_ai_api_visa_ask(request: Request):
    """
    Endpoint to process Visa AI request from frontend.
    Accepts all form fields dynamically.
    """
    try:
        # Get all form fields as dictionary
        data = await request.json()

        # Optional: log to console for debugging
        print("Received form data:", data)

        # Process AI response with all fields
        result = process_visa_request(data)

        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(
            content={"status": "error", "summary": f"Failed to process request: {str(e)}"}
        )
