# app/services/memory.py

from collections import deque

# In production → use Redis
# Here → simulate session memory with LLM standard format
memory_store = {}

def get_context(user_id: str):
    """
    Returns last messages as context in array format
    """
    if user_id not in memory_store:
        memory_store[user_id] = deque(maxlen=10)
    return list(memory_store[user_id])


def save_message(user_id: str, role: str, content: str):
    """
    Stores last N messages per user in standard LLM array format:
    {"role": "user" | "assistant", "content": "..."}
    """
    if user_id not in memory_store:
        memory_store[user_id] = deque(maxlen=10)

    memory_store[user_id].append({"role": role, "content": content})