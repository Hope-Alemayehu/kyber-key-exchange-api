# session_store.py
session_store = {}

def store_keys(session_id: str, public_key: str, private_key: str):
    session_store[session_id] = {"public_key": public_key, "private_key": private_key}

def get_keys(session_id: str):
    return session_store.get(session_id)
