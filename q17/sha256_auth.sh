#!/bin/bash

DB_FILE="auth_db.txt"

touch "$DB_FILE"

# =========================
# Password Strength Checker
# =========================

check_strength() {
    password="$1"
    score=0

    # Length check
    if [ ${#password} -gt 8 ]; then
        ((score++))
    fi

    # Uppercase check
    if [[ "$password" =~ [A-Z] ]]; then
        ((score++))
    fi

    # Lowercase check
    if [[ "$password" =~ [a-z] ]]; then
        ((score++))
    fi

    # Number check
    if [[ "$password" =~ [0-9] ]]; then
        ((score++))
    fi

    # Special character check
    if [[ "$password" =~ [^a-zA-Z0-9] ]]; then
        ((score++))
    fi

    echo "Password Score: $score/5"

    if [ $score -le 2 ]; then
        echo "Password Strength: Weak"
    elif [ $score -le 4 ]; then
        echo "Password Strength: Good"
    else
        echo "Password Strength: Strong"
    fi
}

# =========================
# Generate SHA-256 Hash
# =========================

generate_hash() {
    echo -n "$1" | sha256sum | awk '{print $1}'
}

# =========================
# Register New User
# =========================

register_user() {

    read -p "Enter username: " username

    # Check if username already exists
    if grep -q "^$username:" "$DB_FILE"; then
        echo "Username already exists!"
        return
    fi

    read -s -p "Enter password: " password1
    echo

    read -s -p "Confirm password: " password2
    echo

    if [ "$password1" != "$password2" ]; then
        echo "Passwords do not match!"
        return
    fi

    check_strength "$password1"

    hash=$(generate_hash "$password1")

    echo "$username:$hash" >> "$DB_FILE"

    echo "User registered successfully!"
}

# =========================
# Login User
# =========================

login_user() {

    read -p "Enter username: " username

    stored_hash=$(grep "^$username:" "$DB_FILE" | cut -d ':' -f2)

    if [ -z "$stored_hash" ]; then
        echo "User not found!"
        return
    fi

    read -s -p "Enter password: " password
    echo

    entered_hash=$(generate_hash "$password")

    if [ "$entered_hash" == "$stored_hash" ]; then
        echo "Access Granted"
    else
        echo "Access Denied"
    fi
}

# =========================
# Import Users From File
# =========================

import_users() {

    read -p "Enter file path: " filepath

    if [ ! -f "$filepath" ]; then
        echo "File not found!"
        return
    fi

    username=""
    password=""

    while IFS= read -r line
    do

        if [[ "$line" == u:* ]]; then
            username="${line#u:}"
        fi

        if [[ "$line" == p:* ]]; then
            password="${line#p:}"

            echo
            echo "Processing User: $username"

            check_strength "$password"

            hash=$(generate_hash "$password")

            if grep -q "^$username:" "$DB_FILE"; then
                echo "User already exists. Skipping..."
            else
                echo "$username:$hash" >> "$DB_FILE"
                echo "User imported successfully!"
            fi
        fi

    done < "$filepath"
}

# =========================
# Show Stored Users
# =========================

show_users() {
    echo
    echo "Stored Users:"
    cat "$DB_FILE"
}

# =========================
# Main Menu
# =========================

while true
do

    echo
    echo "========== MENU =========="
    echo "1. New Login / Register"
    echo "2. Login"
    echo "3. Import Users From File"
    echo "4. Show Stored Users"
    echo "5. Exit"
    echo "=========================="

    read -p "Choose option: " choice

    case $choice in

        1)
            register_user
            ;;

        2)
            login_user
            ;;

        3)
            import_users
            ;;

        4)
            show_users
            ;;

        5)
            echo "Exiting..."
            break
            ;;

        *)
            echo "Invalid Option!"
            ;;

    esac

done
