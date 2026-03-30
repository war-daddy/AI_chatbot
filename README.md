# Sachin's AI Assistant

A beautiful, production-grade AI Chatbot built with Python (FastAPI). It serves a sleek, premium glassmorphism chat UI and features an intelligent NLP routing system for local fallback or OpenAI integration.

## Features
- **Premium UI:** A fully responsive, dark-mode glassmorphism interface.
- **Dynamic Suggestions:** Auto-rotating suggestion chips that provide interactive questions about Sachin's professional background.
- **Production AI Pipeline:** Designed to connect to OpenAI's GPT models to dynamically answer questions based on a strict system prompt containing Sachin's resume.
- **Smart Fallback:** No API key? No problem! If no API key is provided, the backend drops into a local fallback mode that intelligently extracts and answers resume questions using keyword density matching.

## How to Run Locally

### 1. Install Dependencies
Ensure you have Python installed (version 3.10+ recommended), then run:
```bash
pip install -r requirements.txt
```

### 2. Environment Setup (Optional)
The application will run perfectly fine out-of-the-box in **local fallback mode**. 

If you want the generative intelligence of OpenAI, create a `.env` file in the root directory and add your key:
```env
OPENAI_API_KEY="sk-your-openai-api-key"
```

### 3. Start the Server
Start the FastAPI server using Uvicorn:
```bash
uvicorn app.main:app --reload --port 8000
```

### 4. Use the App
Open your web browser and navigate to:
**[http://localhost:8000](http://localhost:8000)**

Start chatting using the suggestion chips or type your own questions!
