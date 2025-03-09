
# settings.py
from pydantic_settings import BaseSettings
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from typing_extensions import Annotated
from functools import lru_cache
import re
import os


origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://yourdomain.com",
]

class Settings(BaseSettings):
    app_name: str = "MyFastAPI App"
    OPENAI_KEY: str
    SECRET_KEY: str
    MAX_QUERY_LENGTH: int
    ALLOWED_ORIGINS: List[str] = origins

    class Config:
        env_file = '.env'  # Set your environment variable prefix if needed

@lru_cache()
def get_settings():
    return Settings()

if __name__ == "__main__":
    settings = get_settings()
    print(settings.model_dump())