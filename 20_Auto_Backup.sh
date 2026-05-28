#!/bin/bash
# Shebang
# Tells Linux to execute this script using the Bash shell

# ====================================
# Automated Backup Script
# ====================================

# Source directory to backup
# This is the folder whose data will be compressed
SOURCE_DIR="/home/user/data"

# Backup storage directory
# All compressed backups will be stored here
BACKUP_DIR="/backup"

# Create backup directory if not exists
# mkdir = make directory
# -p = create parent directories if needed
# Also avoids error if directory already exists
mkdir -p "$BACKUP_DIR"

# Timestamp for unique backup file
# $(...) = command substitution
# Runs the date command and stores output in variable
# +"..." = custom date format
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Backup file name
# Creates filename like:
# backup_2026-05-29_00-20-30.tar.gz
# .tar.gz = compressed archive format
BACKUP_FILE="backup_$TIMESTAMP.tar.gz"

# Create compressed backup
# tar = archive utility
# -c = create archive
# -z = compress using gzip
# -f = specify filename
#
# Final output example:
# /backup/backup_2026-05-29_00-20-30.tar.gz
tar -czf "$BACKUP_DIR/$BACKUP_FILE" "$SOURCE_DIR"

# Check if backup successful
# $? stores exit status of previous command
# 0 = success
# non-zero = failure
if [ $? -eq 0 ]; then

    # Display success message
    echo "Backup created successfully:"

    # Print backup file path
    echo "$BACKUP_DIR/$BACKUP_FILE"

else

    # Display failure message
    echo "Backup failed!"

    # exit 1 = terminate script with error status
    exit 1
fi

# Keep only latest 5 backups
#
# ls -1t
# -1 = one file per line
# -t = sort by newest first
#
# Example order:
# backup_5
# backup_4
# backup_3
# backup_2
# backup_1
# backup_old
#
# tail -n +6
# Start displaying from line 6 onward
# Meaning:
# skip latest 5 backups
#
# xargs rm -f
# Pass remaining old files to rm command
#
# rm -f
# force delete old backups
ls -1t "$BACKUP_DIR"/backup_*.tar.gz | tail -n +6 | xargs rm -f

# Final cleanup message
echo "Old backups cleaned. Only last 5 backups kept."
