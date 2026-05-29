#!/bin/bash

echo "===== Last 10 Failed Logins ====="

if [ -f /var/log/auth.log ]; then
    grep "Failed password" /var/log/auth.log | tail -10

elif [ -f /var/log/secure ]; then
    grep "Failed password" /var/log/secure | tail -10

else
    journalctl | grep "Failed password" | tail -10
fi
