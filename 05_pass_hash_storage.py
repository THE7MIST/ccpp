#!/usr/bin/env python3

# ====================================
# Password Strength + Hash Storage
# ====================================

import hashlib
import re

HASH_FILE = "password.hash"

def password_strength(password):

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[@$!%*?&]", password):
        return False

    return True


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Registration
password = input("Create Password: ")

if not password_strength(password):
    print("Weak Password")
    exit()

hashed = hash_password(password)

with open(HASH_FILE, "w") as f:
    f.write(hashed)

print("Password Stored Successfully")


# Login Verification
login_password = input("\nLogin Password: ")

login_hash = hash_password(login_password)

with open(HASH_FILE, "r") as f:
    stored_hash = f.read().strip()

if login_hash == stored_hash:
    print("Login Successful")
else:
    print("Invalid Password")
