#!/usr/bin/env python3

# ====================================
# Advanced Email + IP + URL Extractor
# ====================================

import re

filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        data = file.read()

    # Email Regex
    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        data
    )

    # IPv4 Regex
    ips = re.findall(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        data
    )

    # URL Regex
    urls = re.findall(
        r'https?://[^\s]+',
        data
    )

    print("\n===== EMAILS =====")
    for email in emails:
        print(email)

    print("\n===== IPv4 ADDRESSES =====")
    for ip in ips:
        print(ip)

    print("\n===== URLs =====")
    for url in urls:
        print(url)

except FileNotFoundError:
    print("File not found!")



#!/bin/bash

# ====================================
# Advanced Email + IP + URL Extractor
# ====================================

read -p "Enter filename: " FILE

echo "===== EMAILS ====="
grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$FILE"

echo
echo "===== IPv4 ADDRESSES ====="
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' "$FILE"

echo
echo "===== URLs ====="
grep -oE 'https?://[^ ]+' "$FILE"
