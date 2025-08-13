import os
from dotenv import load_dotenv

load_dotenv()

class BaseClient:
    def __init__(self, token_env: str, base_url: str, headers: dict | None = None):
        token = os.getenv(token_env)
        if not token:
            raise RuntimeError(f"Env var {token_env} is empty")
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}
        self.headers.setdefault("Authorization", token)
