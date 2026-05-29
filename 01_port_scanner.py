#!/usr/bin/env python3

# ====================================
# Enhanced Port Scanner
# ====================================

import socket

target = input("Enter Hostname/IP: ")

try:
    target_ip = socket.gethostbyname(target)

    print(f"\nScanning Target: {target}")
    print(f"Resolved IP   : {target_ip}")
    print("-" * 40)

    for port in range(1, 1025):

        sock = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)

        sock.settimeout(0.5)

        result = sock.connect_ex((target_ip, port))

        if result == 0:

            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            print(f"Port {port:<5} OPEN ({service})")

        sock.close()

except socket.gaierror:
    print("Unable to resolve hostname.")

except KeyboardInterrupt:
    print("\nScan interrupted.")
