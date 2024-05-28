## Håstad's broadcast attack

from Crypto.Util.number import getPrime
from Crypto.Util.number import bytes_to_long
from math import gcd 

e = 5
flag = "CS2107{test_flag_not_actual_flag}"
assert len(flag) <= 64

flag = bytes_to_long(flag.encode())
output_file = open('output.txt', 'w')

# Generate the encrypted flag with 5 different RSA key
for _ in range(e):
    while True:
        p = getPrime(512)
        q = getPrime(512)
        n_i = p * q 
        phi = (p - 1) * (q - 1)

        if gcd(phi, e) == 1: 
            break 
    
    a_i = getPrime(1024)
    b_i = getPrime(1024)
    m_i = a_i * flag + b_i
    c_i = pow(m_i, e, n_i)

    output_file.write(f'{str(a_i)}\n')
    output_file.write(f'{str(b_i)}\n')
    output_file.write(f'{str(c_i)}\n')
    output_file.write(f'{str(n_i)}\n')
