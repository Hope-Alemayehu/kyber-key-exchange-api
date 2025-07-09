from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional
import uuid

from app.crypto_utils import generate_keys, encapsulate_key, decapsulate_key
from app.session_store import SessionStore

app = FastAPI(
    title="Kyber Key Exchange API",
    description="A Post-Quantum Cryptography key exchange service using Kyber",
    version="1.0.0",
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize session store
session_store = SessionStore()


# Request/Response models
class KeyPairResponse(BaseModel):
    session_id: str
    public_key: str
    private_key: str


class ExchangeRequest(BaseModel):
    session_id: str
    peer_public_key: str


class ExchangeResponse(BaseModel):
    ciphertext: str
    shared_secret: str


class DecapsulateRequest(BaseModel):
    session_id: str
    ciphertext: str


# API Endpoints
@app.get("/")
async def root():
    return {
        "message": "Kyber Key Exchange API - Use /docs for interactive documentation"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/generate-keypair", response_model=KeyPairResponse)
async def generate_keypair():
    """Generate a new keypair and store it in the session."""
    public_key, private_key = generate_keys()
    session_id = str(uuid.uuid4())

    # Store the private key in the session
    session_store.set(session_id, {"private_key": private_key})

    return {
        "session_id": session_id,
        "public_key": public_key,
        "private_key": private_key,  # In production, never return the private key to the client
    }


@app.post("/exchange", response_model=ExchangeResponse)
async def exchange_keys(request: ExchangeRequest):
    """
    Perform a key exchange using the peer's public key.
    Returns the ciphertext and shared secret.
    """
    try:
        # In a real application, you would validate the session exists
        session = session_store.get(request.session_id)
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")

        ciphertext, shared_secret = encapsulate_key(request.peer_public_key)

        # Store the shared secret in the session
        session["shared_secret"] = shared_secret
        session_store.set(request.session_id, session)

        return {"ciphertext": ciphertext, "shared_secret": shared_secret}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/decapsulate")
async def decrypt_shared_secret(request: DecapsulateRequest):
    """
    Decapsulate a shared secret using the private key from the session.
    This demonstrates the other side of the key exchange.
    """
    try:
        session = session_store.get(request.session_id)
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")

        if "private_key" not in session:
            raise HTTPException(
                status_code=400, detail="No private key found in session"
            )

        shared_secret = decapsulate_key(session["private_key"], request.ciphertext)

        # Store the shared secret in the session
        session["shared_secret"] = shared_secret
        session_store.set(request.session_id, session)

        return {"shared_secret": shared_secret}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
