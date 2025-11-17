import os
from dotenv import load_dotenv

load_dotenv()

NUMVERIFY_API_KEY = os.getenv("NUMVERIFY_API_KEY")

if not NUMVERIFY_API_KEY:
    raise ValueError("NUMVERIFY_API_KEY is missing from .env")
