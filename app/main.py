from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.crypto_utils import generate_keys, encapsulate_key
from app.session_store import store_keys, get_keys

app = FastAPI()

class SessionRequest(BaseModel):
    session_id: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/generate-keypair")
def generate_keypair_endpoint(request: SessionRequest):
    public_key, private_key = generate_keys()
    store_keys(request.session_id, public_key, private_key)
    return {
        "session_id": request.session_id,
        "public_key": public_key
    }

class ExchangeRequest(BaseModel):
    session_id: str
    peer_public_key: str

@app.post("/exchange")
def exchange_endpoint(request: ExchangeRequest):
    # Check if session exists
    keys = get_keys(request.session_id)
    if not keys:
        raise HTTPException(status_code=404, detail="Session ID not found")
    
    ciphertext, shared_secret = encapsulate_key(request.peer_public_key)
    
    return {
        "ciphertext": ciphertext,
        "shared_secret": shared_secret
    }
