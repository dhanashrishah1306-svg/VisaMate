# app/services/ai_service.py

from app.core.config import GEMINI_API_KEY
import google.generativeai as genai

# Configure API key
genai.configure(api_key=GEMINI_API_KEY)

# Use stable and working model
model = genai.GenerativeModel("gemini-2.5-flash")


def build_prompt(data: dict) -> str:
    """
    Builds a STRICT prompt to force clean, frontend-friendly output.
    """

    prompt_lines = [
        "You are a professional visa consultant.",
        "",
        "OUTPUT RULES (VERY IMPORTANT):",
        "Do not use bullet symbols, stars, dashes, or numbering.",
        "Do not use markdown or special formatting.",
        "Do not bold anything.",
        "Each line must follow this exact format:",
        "Document Name: One-line explanation. Official link if available.",
        "One document per line.",
        "",
        "Applicant Details:"
    ]

    # Core fields (do NOT change field names)
    main_fields = [
        "name",
        "gender",
        "purpose",
        "continent",
        "destination_country",
        "nationality",
        "duration",
        "education_level",
        "employment_status",
        "extra_question"
    ]

    for field in main_fields:
        if field in data and data[field]:
            prompt_lines.append(f"{field.replace('_', ' ').title()}: {data[field]}")

    # Dynamic extra fields from frontend
    extra_fields = data.get("extra_fields", {})
    if extra_fields:
        prompt_lines.append("")
        prompt_lines.append("Additional Details:")
        for key, value in extra_fields.items():
            if value:
                prompt_lines.append(f"{key.replace('_', ' ').title()}: {value}")

    prompt_lines.extend([
        "",
        "Now generate visa guidance.",
        "Include only required documents first.",
        "After documents, add a section title exactly as:",
        "Next Steps",
        "Under Next Steps, follow the SAME format (no bullets, no numbering)."
    ])

    return "\n".join(prompt_lines)


def process_visa_request(data: dict):
    """
    Generates structured visa guidance compatible with frontend formatting.
    """
    try:
        response = model.generate_content(
            build_prompt(data),
            generation_config={
                "temperature": 0.3,
                "max_output_tokens": 40000
            }
        )

        return {
            "status": "success",
            "summary": response.text.strip()
        }

    except Exception as e:
        return {
            "status": "error",
            "summary": f"Failed to generate AI response: {str(e)}"
        }
