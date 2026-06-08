from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from bedrock_service import generate_ai_response
from lead_service import save_lead, get_leads, init_db

app = FastAPI(title="IT Sales Demo Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

class ChatRequest(BaseModel):
    message: str

class LeadRequest(BaseModel):
    name: str
    company: str
    email: str
    phone: str
    requirement: str
    company_size: int
    timeline: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
    reply = generate_ai_response(req.message)
    return {"reply": reply}

@app.post("/lead")
def create_lead(req: LeadRequest):
    score = save_lead(req.dict())
    return {
        "status": "saved",
        "lead_score": score
    }

@app.get("/leads")
def list_leads():
    return get_leads()
