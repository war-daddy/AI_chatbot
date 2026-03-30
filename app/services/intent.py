# app/services/intent.py

def detect_intent(message: str):
    """
    Simple rule-based intent detection.
    You can upgrade this later using ML.
    """
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "greeting"

    if "name" in message:
        return "ask_name"

    if "remember" in message:
        return "store_memory"

    if "what did i say" in message:
        return "recall_memory"

    return "fallback"