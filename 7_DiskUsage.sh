#!/bin/bash

df -h | grep '^/dev/' | while read line
do
    usage=$(echo $line | awk '{print $5}' | sed 's/%//')
    partition=$(echo $line | awk '{print $6}')

    if (( usage > 80 )); then
        echo "$(date) WARNING: $partition usage is at ${usage}%" >> /var/log/disk_alert.log
    fi
done
