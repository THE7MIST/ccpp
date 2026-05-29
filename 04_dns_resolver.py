#!/usr/bin/env python3

# ====================================
# DNS Resolver Tool
# ====================================

import socket

domain = input("Enter domain name: ")

try:

    ip_address = socket.gethostbyname(domain)

    print("\nIP Address :", ip_address)

    try:

        hostname, alias, address = socket.gethostbyaddr(
            ip_address
        )

        print("Reverse DNS:", hostname)

    except socket.herror:

        print("Reverse DNS: Not Available")

except socket.gaierror:

    print("Unable to resolve domain.")
