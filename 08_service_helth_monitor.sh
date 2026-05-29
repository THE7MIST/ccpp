#!/bin/bash

LOG_FILE="/var/log/service_monitor.log"

SERVICES=("sshd" "nginx" "apache2" "httpd" "mysql" "mariadb")

for service in "${SERVICES[@]}"
do
    systemctl list-unit-files | grep -q "^${service}.service"

    if [ $? -eq 0 ]
    then
        if ! systemctl is-active --quiet "$service"
        then
            echo "$(date) - Restarting $service" >> "$LOG_FILE"

            systemctl restart "$service"

            echo "$(date) - $service restarted" >> "$LOG_FILE"
        fi
    fi
done
