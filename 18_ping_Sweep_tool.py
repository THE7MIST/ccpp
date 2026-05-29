#!/usr/bin/env python3

# ====================================
# Ping Sweep Tool
# ====================================

import ipaddress
import subprocess

# Get subnet from user
subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")

try:
    network = ipaddress.ip_network(subnet, strict=False)

    print(f"\nScanning subnet: {network}")
    print("-" * 40)

    live_hosts = []

    for ip in network.hosts():
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", str(ip)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:
            print(f"[+] Host Alive: {ip}")
            live_hosts.append(str(ip))

    print("\nScan Complete")
    print(f"Total Live Hosts: {len(live_hosts)}")

except ValueError:
    print("Invalid subnet entered!")
