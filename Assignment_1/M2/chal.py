from Crypto.Cipher import AES
from random import randbytes
from Crypto.Util.Padding import pad

cipher = AES.new(randbytes(16),AES.MODE_ECB)
secret = "CS2107{[REDACTED][REDACTED][REDACTED][REDAC}"
code = open("chal.py","rb").read()

with open("output","wb") as f:
    for i in code:
        f.write(cipher.encrypt(pad(bytes([i]),16)))
