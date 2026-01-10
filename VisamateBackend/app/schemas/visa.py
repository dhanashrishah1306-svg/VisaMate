from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VisaRequest(BaseModel):
    name: Optional[str]
    gender: Optional[str]
    purpose: str
    continent: str
    destination_country: str
    nationality: str
    duration: Optional[str]

    # Kept for backward compatibility (optional use)
    education_level: Optional[str] = None
    employment_status: Optional[str] = None

    # This captures ALL purpose-specific & hidden fields
    extra_fields: Dict[str, Any] = Field(default_factory=dict)


class VisaResponse(BaseModel):
    status: str
    summary: str
