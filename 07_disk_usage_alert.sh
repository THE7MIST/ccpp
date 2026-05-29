#!/bin/bash

# ==========================
# Disk Usage Alert Script
# ==========================

LOG_FILE="/var/log/disk_alert.log"
THRESHOLD=80

df -h | grep '^/dev/' | while read line
do
    usage=$(echo "$line" | awk '{gsub("%",""); print $5}')
    partition=$(echo "$line" | awk '{print $6}')

    if [ "$usage" -gt "$THRESHOLD" ]
    then
        echo "$(date) WARNING: $partition usage is ${usage}%" >> "$LOG_FILE"

        echo "Alert Logged for $partition"
    fi
done
