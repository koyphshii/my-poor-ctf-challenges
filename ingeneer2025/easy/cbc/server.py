#!/usr/local/bin/python3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def decrypt(data, key):
    iv = data[:16]
    ct = data[16:]
    if len(ct) != 48 or len(iv) != 16:
        return None
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(ct)

key = get_random_bytes(16)
ct = os.urandom(48)
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(ct)
target = os.urandom(48)

print("CT:")
print(ct.hex())
print("Initial plaintext:")
print(pt.hex())
print("Target:")
print(target.hex())
print("IV:")
print(iv.hex())

try:
    print("Send iv + ciphertext (hex):")
    data = input(">>> ").strip()
    user_input = bytes.fromhex(data)
    m = decrypt(user_input, key)
    
    if m and m[:16] == target[:16] and m[32:] == target[32:]:
        with open('flag.txt', 'rb') as f:
            flag = f.read()
        print("Correct! Here is your flag:")
        print(flag.decode())
    else:
        print("Wrong input.")
except Exception as e:
    print("Error.")
