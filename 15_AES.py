#!/usr/bin/env python3

# ====================================
# AES Encryption / Decryption Tool
# ====================================

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
import base64

# Generate a 32-byte AES key from password
def generate_key(password):
    return sha256(password.encode()).digest()

# Encrypt Function
def encrypt(text, password):
    key = generate_key(password)

    cipher = AES.new(key, AES.MODE_CBC)

    ciphertext = cipher.encrypt(
        pad(text.encode(), AES.block_size)
    )

    encrypted_data = (
        cipher.iv + ciphertext
    )

    return base64.b64encode(encrypted_data).decode()

# Decrypt Function
def decrypt(encrypted_text, password):
    key = generate_key(password)

    encrypted_data = base64.b64decode(encrypted_text)

    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    plaintext = unpad(
        cipher.decrypt(ciphertext),
        AES.block_size
    )

    return plaintext.decode()


# Main Program
message = input("Enter message: ")
password = input("Enter password: ")

encrypted = encrypt(message, password)

print("\nEncrypted Text:")
print(encrypted)

decrypted = decrypt(encrypted, password)

print("\nDecrypted Text:")
print(decrypted)
