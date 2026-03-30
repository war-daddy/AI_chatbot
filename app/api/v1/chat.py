# app/api/v1/chat.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_engine import chat

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str

@router.post("/chat")
def chat_api(req: ChatRequest):
    """
    Chat endpoint with memory support
    """
    response = chat(req.user_id, req.message)

    return {"response": response}