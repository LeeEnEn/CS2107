from base64 import b64encode, b64decode
from Crypto.Cipher import AES # pip3 install pycryptodome
import hashlib
import json
import secrets

nonce = b64decode('RU843NtgjL0=')
cipher_text = b64decode('SHO454D67I/rC5m79uiSg49m9w0rEHzHd+wXHuBSGwuDx3906yjFs3hwFOo5MJcG')

for x in range(1, 2 ** 25):
  key = hashlib.sha256(str(x).encode()).digest()

  cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
  plain_text = cipher.decrypt(cipher_text)

  try:
    plain_text = plain_text.decode('utf-8')

    if plain_text[0] == 'C':
      print(x, plain_text)
      break
  except:
    pass