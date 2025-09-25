from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
import os
import httpx
import uvicorn


load_dotenv()
HUBSPOT_TOKEN = os.getenv("HUBSPOT_ACCESS_TOKEN")
BASE_URL = os.getenv("BASE_URL")
if not HUBSPOT_TOKEN:
    raise ValueError("HUBSPOT_ACCESS_TOKEN not set in .env file")

class ContactRequest(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr

# Service layer
class HubSpotService:

    def __init__(self, token: str):
        self.token = token

    async def create_contact(self, contact: ContactRequest):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "properties": contact.dict()
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(BASE_URL, headers=headers, json=payload)

        if response.status_code >= 400:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )
        return response.json()

app = FastAPI()
hubspot_service = HubSpotService(HUBSPOT_TOKEN)

@app.post("/contacts")
async def create_contact(contact: ContactRequest):
    return await hubspot_service.create_contact(contact)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
