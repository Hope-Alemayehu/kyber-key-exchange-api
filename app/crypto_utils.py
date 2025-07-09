import os
import base64

def generate_keys():
    # Simulate Kyber 512-bit public and 1024-bit private keys
    public_key = os.urandom(512 // 8)    # 64 bytes
    private_key = os.urandom(1024 // 8)  # 128 bytes
    
    public_key_b64 = base64.b64encode(public_key).decode()
    private_key_b64 = base64.b64encode(private_key).decode()
    
    return public_key_b64, private_key_b64

def encapsulate_key(peer_public_key_b64):
    # Simulate encapsulation by generating random ciphertext + shared secret
    ciphertext = os.urandom(256 // 8)   # 32 bytes ciphertext
    shared_secret = os.urandom(256 // 8) # 32 bytes shared secret
    
    return base64.b64encode(ciphertext).decode(), base64.b64encode(shared_secret).decode()
