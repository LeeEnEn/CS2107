import random 
import os 

def encrypt(msg, key):
    return bytes(a ^ b for a, b in zip(msg, key))

def xor_secure(keys, msg):
    result = msg

    for key in keys:
        result = encrypt(result, key)
    
    return result 

if __name__ == "__main__":
    # Secret message
    msg = "CS2107{dummy_flag_not_actual_flag}"
    msg = msg.encode()
    
    # Generating keys
    key_length = len(msg)
    key1 = random.randbytes(key_length)
    key2 = os.urandom(key_length)
    key3 = b'A' * (key_length)
    key4 = bytes([random.randint(0, 255) for _ in range(len(msg))])

    keys = [key1, key2, key3, key4]

    # Encrypt the message
    enc_msg = xor_secure(keys, msg)
    
    # Print out the encryption output
    print(f'key1 = "{key1.hex()}"')
    print(f'key2 = "{key2.hex()}"')
    print(f'key3 = "{key3.hex()}"')
    print(f'key4 = "{key4.hex()}"')
    print(f'enc_msg = "{enc_msg.hex()}"')