from cryptography.fernet import Fernet
import sqlite3
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

def setup_database():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                    (id INTEGER PRIMARY KEY,) service TEXT, username Text, password TEXT)''')
    conn.commit()
    conn.close()

def add_password(service, username, password, key):
    encrypted_password = encrypt_password(password, key)
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
              (service, username, encrypted_password))
    conn.commit()
    conn.close()

def get_password(service, key):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT username, password FROM passwords WHERE service=?", (service,))
    result = c.fetchone()
    conn.close()
    if result:
        username, encrypted_password = result
        decrypted_password = decrypt_password(encrypted_password, key)
        return username, decrypted_password
    else:
        return None
    
def main():
    if not os.path.exists("secret.key"):
        generate_key()
    key = load_key()
    setup_database()

    while True:
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(service, username, password, key)
            print("Password added successfully!")
        elif choice == "2":
            service = input("Enter the service name: ")
            result = get_password(service, key)
            if result:
                username, password = result
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print("No password found for this service.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()