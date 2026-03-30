# app/core/config.py
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # LLM Settings
    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = "gpt-4o-mini"
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = "ignore" # ignores extra variables in .env if any

settings = Settings()
