# app/services/response.py

def generate_response(intent, message, context):
    """
    Generates response based on intent + memory context
    """

    if intent == "greeting":
        return "Hello! How can I help you today?"

    if intent == "ask_name":
        return "I am your local AI assistant 🤖"

    if intent == "store_memory":
        return f"Got it. I'll remember: {message}"

    if intent == "recall_memory":
        return f"You said: {context}"

    return "Sorry, I didn't understand that."