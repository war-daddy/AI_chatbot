# app/services/chat_engine.py

from app.services.memory import save_message, get_context
from app.core.config import settings
from app.core.prompt import SYSTEM_PROMPT
import logging

try:
    from openai import OpenAI
    # Only establish real client if key exists
    client = OpenAI(api_key=settings.OPENAI_API_KEY) if settings.OPENAI_API_KEY else None
except ImportError:
    client = None

logging.basicConfig(level=logging.INFO)

def chat(user_id: str, message: str) -> str:
    """
    Core production pipeline:
    1. Save user msg
    2. Build context payload (System + Memory)
    3. Call LLM (or fallback mock)
    4. Save AI msg
    5. Return
    """
    
    # Step 1: store user message
    save_message(user_id, "user", message)
    
    # Step 2: get context
    history = get_context(user_id)
    
    # Step 3: Build standard payload
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history

    # Step 4: Call LLM
    response_text = ""
    
    if client and settings.OPENAI_API_KEY:
        try:
            completion = client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            response_text = completion.choices[0].message.content
        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
            response_text = "Sorry, I encountered an error connecting to my language processor."
    else: # Fallback keyword-based mock
        response_text = _fallback_resume_response(message)
    
    # Step 5: save AI msg and return
    save_message(user_id, "assistant", response_text)
    return response_text


def _fallback_resume_response(message: str) -> str:
    msg = message.lower()
    
    if "hello" in msg or "hi" in msg or "hey" in msg:
        return "Hello! I am Sachin Kumar's AI assistant. How can I help you today?"
    
    if "loop" in msg or "eloop" in msg or "current" in msg or "present" in msg:
        return "Sachin is currently a Full Stack Engineer at eLoop Dev Solutions LLP (Nov 2024 - Present). He works heavily on a React/Redux/Node.js internal CMS, implementing robust data grids, integrating Gen-AI assisted panels, and collaborating across teams."
        
    if "10times" in msg or "hubs" in msg:
        return "Sachin was previously a Software Engineer (Frontend - React) at 10Times from May 2023 to Nov 2024, building community Hubs features for over 2M users using React, Redux, and custom hooks."
        
    if "experience" in msg or "work" in msg:
        return "Sachin has 2.5+ years of experience as a Frontend-focused Full Stack Engineer. He worked at 10Times scaling features for 2M+ users, and currently works at eLoop Dev Solutions building an internal CMS and Gen-AI tools."
        
    if "react" in msg or "next" in msg or "frontend" in msg or "stack" in msg or "tech" in msg or "skill" in msg:
        return "Sachin specializes in Frontend Engineering (React.js, Redux Toolkit, Next.js, Tailwind CSS) but is also highly comfortable across the backend with Node.js, Express, and APIs."
        
    if "database" in msg or "mysql" in msg or "postgresql" in msg or "mongodb" in msg or "schema" in msg:
        return "Sachin has solid experience designing and operating databases, specifically working with MongoDB, MySQL, and PostgreSQL across his full stack roles."
        
    if "education" in msg or "college" in msg or "degree" in msg or "cgpa" in msg or "b.tech" in msg:
        return "Sachin holds a B.Tech in Computer Science Engineering from R.G.P.V (2019-2023) with an excellent CGPA of 8.95."
        
    if "certif" in msg or "nptel" in msg or "iit" in msg:
        return "Sachin holds a prestigious certification in Design and Analysis of Algorithms from IIT Madras (via NPTEL)."
        
    if "performance" in msg or "render" in msg:
        return "At 10Times, Sachin specifically focused on UI performance by reducing unnecessary re-renders in React and reorganizing component boundaries for complex nested discussions."
        
    if "gen-ai" in msg or "ai" in msg or "llm" in msg:
        return "At eLoop Dev Solutions, Sachin integrated a Gen-AI assisted panel to help internal teams with repetitive tasks, handling async flows, loading states, and error cases on the frontend."
        
    if "admin" in msg or "internal tool" in msg or "cms" in msg:
        return "Sachin built a database-like internal CMS web interface with structured datasets, spreadsheet-style inline editing, and validation at eLoop Dev Solutions."
        
    if "hire" in msg or "why sachin" in msg:
        return "You should hire Sachin because he brings 2.5+ years of production experience shipping high-traffic features (2M+ users), a deep expertise in React and state management, and the full-stack capability to collaborate seamlessly with backend teams."

    return "I am operating in a fallback knowledge mode. Please ask me specific keywords about Sachin's 'experience', 'college', 'skills', or 'certifications'."