#!/bin/bash

# ===============================
# Cron Job Verifier
# ===============================

echo "===== Current User Cron Jobs ====="
crontab -l

echo
read -p "Enter keyword/job to search: " JOB

if crontab -l | grep -q "$JOB"
then
    echo "Cron job found."
else
    echo "Cron job NOT found."
fi
