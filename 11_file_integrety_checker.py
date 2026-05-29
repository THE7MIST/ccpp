#!/usr/bin/env python3

# ====================================
# File Integrity Checker
# ====================================

import os
import json
import hashlib

HASH_FILE = "file_hashes.json"

directory = input("Enter directory to monitor: ")

def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

current_hashes = {}

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)

        try:
            current_hashes[filepath] = calculate_hash(filepath)
        except Exception:
            pass

# First Run
if not os.path.exists(HASH_FILE):
    with open(HASH_FILE, "w") as f:
        json.dump(current_hashes, f, indent=4)

    print("Baseline hashes stored.")
    exit()

# Load Previous Hashes
with open(HASH_FILE, "r") as f:
    old_hashes = json.load(f)

print("\n===== FILE INTEGRITY REPORT =====")

# New Files
for file in current_hashes:
    if file not in old_hashes:
        print(f"[NEW] {file}")

# Deleted Files
for file in old_hashes:
    if file not in current_hashes:
        print(f"[DELETED] {file}")

# Modified Files
for file in current_hashes:
    if file in old_hashes:
        if current_hashes[file] != old_hashes[file]:
            print(f"[MODIFIED] {file}")

# Update Baseline
with open(HASH_FILE, "w") as f:
    json.dump(current_hashes, f, indent=4)
