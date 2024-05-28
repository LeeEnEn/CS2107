from base64 import b64encode
from Crypto.Cipher import AES # pip3 install pycryptodome
import hashlib 
import json
import secrets 


def generate_key(limit):
    private_key = secrets.randbelow(limit)

    return hashlib.sha256(str(private_key).encode()).digest()

def encrypt(msg):
    # Should be strong enough, 25 for 2025 future proof!!
    limit = 2 ** 25
    key = generate_key(limit)

    cipher = AES.new(key, AES.MODE_CTR)
    ct_bytes = cipher.encrypt(msg)
    nonce = b64encode(cipher.nonce).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    
    result = json.dumps({'nonce': nonce, 'ciphertext': ct})
    return result 

if __name__ == "__main__":
    msg = "<some_secret_message_was_here>"
    msg = msg.encode()

    print(encrypt(msg))