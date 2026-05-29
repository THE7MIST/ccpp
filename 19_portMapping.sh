#!/bin/bash

# ====================================
# Process + Port Mapping
# ====================================

echo "-----------------------------------------------"
printf "%-20s %-10s %-10s\n" "PROCESS" "PID" "PORT"
echo "-----------------------------------------------"

ss -tulnp | awk '
NR>1 {
    split($5, a, ":")

    port = a[length(a)]

    process = $NF

    gsub(/users:\(\("/, "", process)
    gsub(/".*/, "", process)

    pid = $NF
    match(pid, /pid=[0-9]+/)

    if (RSTART > 0) {
        pid = substr(pid, RSTART+4, RLENGTH-4)
    } else {
        pid = "N/A"
    }

    printf "%-20s %-10s %-10s\n", process, pid, port
}'


#ss -tulnp | awk 'NR>1 {split($5,a,":"); print $NF,"\t",a[length(a)]}'
