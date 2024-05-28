import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from base64 import b64decode
from random import randbytes

m_dict = {}

t = b''

with open("output", "rb") as f:
    t = f.read()

f.close()

with open("chal.py", "r") as f:
    lines = f.read()
    
    for x in range(len(lines)):
        v = ord(lines[x])
        b = t[x * 16: (x + 1) * 16]
        
        if x < 151 or x > 194:
            m_dict[b] = v
        if x == 153:
            m_dict[b] = ord('2')
        if x == 154:
            m_dict[b] = ord('1')
        if x == 155:
            m_dict[b] = ord('0')
        if x == 156:
            m_dict[b] = ord('7')
    
f.close()

flag = ''
start = 151
for x in range(158, 194):
    b = t[x * 16: (x + 1) * 16]
    flag += chr(m_dict[b])

print(flag)
