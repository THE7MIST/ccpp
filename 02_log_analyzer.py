#!/usr/bin/env python3

# ====================================
# Log Analyzer
# ====================================

from collections import Counter

log_file = input("Enter log file path: ")

total_requests = 0
error_404 = 0
ip_counter = Counter()

with open(log_file, "r") as f:
    for line in f:

        total_requests += 1

        parts = line.split()

        if len(parts) > 0:
            ip_counter[parts[0]] += 1

        if " 404 " in line:
            error_404 += 1

print("\n===== LOG ANALYSIS =====")
print("Total Requests :", total_requests)
print("404 Errors     :", error_404)

print("\nTop 3 IP Addresses:")

for ip, count in ip_counter.most_common(3):
    print(f"{ip} -> {count} requests")
