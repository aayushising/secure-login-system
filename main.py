import sqlite3
import hashlib
from database import create_connection

# Hash password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register user
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hash_password(password)

    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Parameterized query prevents SQL Injection
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, hashed_password))
        conn.commit()
        print("User registered successfully!")
    except:
        print("Username already exists.")

    conn.close()


# Login user
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hash_password(password)

    conn = create_connection()
    cursor = conn.cursor()

    # Parameterized query prevents SQL Injection
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username, hashed_password))

    result = cursor.fetchone()

    if result:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    conn.close()


# Menu
while True:
    print("\n--- Secure Login System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        break

    else:
        print("Invalid choice")
