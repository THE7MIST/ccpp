#!/usr/bin/env python3

# ====================================
# Network Interface Analyzer
# ====================================

import psutil
import socket

interfaces = psutil.net_if_addrs()
stats = psutil.net_if_stats()

print("-" * 75)
print(f"{'Interface':15} {'IP Address':20} {'MAC Address':20} {'Status'}")
print("-" * 75)

for interface, addresses in interfaces.items():

    ip_address = "N/A"
    mac_address = "N/A"

    for addr in addresses:

        if addr.family == socket.AF_INET:
            ip_address = addr.address

        elif str(addr.family) == "AddressFamily.AF_PACKET":
            mac_address = addr.address

    status = "UP" if stats[interface].isup else "DOWN"

    print(
        f"{interface:15} "
        f"{ip_address:20} "
        f"{mac_address:20} "
        f"{status}"
    )
