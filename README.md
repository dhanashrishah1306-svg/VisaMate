# VisaMate – Almenda Hacks Project 

VisaMate is an AI-powered visa guidance platform that helps users generate accurate visa document checklists 
and guidance for various countries based on their travel purpose, nationality, and other personal details.
Built with Python (FastAPI backend) and HTML/CSS/JS frontend.

## Features
1. Generates structured visa guidance dynamically for different visa types (work, study, travel, etc.)
2. Supports multiple countries and continents
3. AI-assisted document checklist with clear instructions and links
4. Responsive frontend with user-friendly form interface
5. Handles single or group travelers

## Tech Stack
1. Backend: Python, FastAPI
2. AI Service: Google Gemini API
3. Frontend: HTML, CSS, JavaScript, Bootstrap
4. Deployment-ready structure

## Installation
1. Clone the repository
git clone https://github.com/dhanashrishah1306-svg/VisaMate.git
cd VisaMate

2. Create and activate a virtual environment
python -m venv venv

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set API key
Add your AI API key in VisamateBackend/app/core/config.py:
GEMINI_API_KEY = "YOUR_API_KEY_HERE"

5. Run the backend
uvicorn VisamateBackend.app.main:app --reload

6. Open the frontend
Open VisamateFrontend/index.html in your browser.

## Usage
Select travel purpose and fill out the form
Choose continent and destination country
Fill in personal, employment, and educational details
Submit the form to get an AI-generated, structured visa guidance checklist

Folder Structure
VisamateBackend/       ( Backend API and services)
VisamateFrontend/      ( HTML, CSS, JS files )
requirements.txt       ( Python dependencies )

## Contribution
Ensure .env or API keys are not committed
Fork the repo, create a branch, and submit PRs for improvements
Contact the maintainer for collaboration

## License
This project is open-source for hackathon use.
![Project Thumbnail](VisaMateFrontEnd/imgs/VisaMateLogo.jpg)
