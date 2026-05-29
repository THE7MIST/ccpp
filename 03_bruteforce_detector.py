#!/usr/bin/env python3

# ====================================
# SSH Brute Force Detector
# ====================================

import re
from collections import Counter

LOG_FILE = "/var/log/auth.log"

failed_ips = Counter()

try:

    with open(LOG_FILE, "r") as f:

        for line in f:

            if "Failed password" in line:

                match = re.search(
                    r'from (\d+\.\d+\.\d+\.\d+)',
                    line
                )

                if match:
                    ip = match.group(1)
                    failed_ips[ip] += 1

    print("\n===== Suspicious IPs =====")

    found = False

    for ip, count in failed_ips.items():

        if count > 5:
            found = True
            print(
                f"Suspicious IP: {ip} "
                f"({count} failed attempts)"
            )

    if not found:
        print("No brute-force activity detected.")

except FileNotFoundError:
    print("Log file not found.")
