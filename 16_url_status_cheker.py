#!/usr/bin/env python3

# ====================================
# URL Status Checker
# ====================================

import requests
import time

urls = []

print("Enter URLs (type 'done' to finish):")

while True:
    url = input("URL: ")

    if url.lower() == "done":
        break

    urls.append(url)

print("\nChecking URLs...")
print("-" * 60)

for url in urls:
    try:
        start = time.time()

        response = requests.get(url, timeout=5)

        end = time.time()

        response_time = round((end - start) * 1000, 2)

        print(f"URL          : {url}")
        print(f"Status Code  : {response.status_code}")
        print(f"Response Time: {response_time} ms")
        print("-" * 60)

    except requests.exceptions.RequestException as e:
        print(f"{url} -> ERROR: {e}")
