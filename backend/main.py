from fastapi import FastAPI
from phone_lookup import lookup_number

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Phone Lookup API is running"}

@app.get("/lookup")
def lookup(phone: str):
    return lookup_number(phone)
