# OPS401D10  Ops Challenge 07
# 01/17/2024
# Dominique Bruso
# source: https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/; https://chat.openai.com/share/a844a1bd-7c25-45b2-ac75-bab228d1ff20

#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet, InvalidToken

# Function to generate and save a secret key for encryption
def generate_and_save_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Function to load the saved encryption key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(filename, key):
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
    except (IOError, PermissionError) as e:
        print(f"Error encrypting {filename}: {e}")

# Function to decrypt a file
def decrypt_file(filename, key):
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
    except (IOError, PermissionError) as e:
        print(f"Error decrypting {filename}: {e}")
    except InvalidToken:
        print(f"Decryption failed for {filename}: Invalid key or corrupted data")

# Function to encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    try:
        return f.encrypt(message.encode())
    except InvalidToken:
        print("Invalid encryption token.")
        return None

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    try:
        return f.decrypt(encrypted_message).decode()
    except InvalidToken:
        print("Invalid decryption token. Decryption failed.")
        return None

def encrypt_directory(path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as file_to_encrypt:
                    file_data = file_to_encrypt.read()
                encrypted_data = f.encrypt(file_data)
                with open(file_path, "wb") as file_to_write:
                    file_to_write.write(encrypted_data)
            except (IOError, PermissionError) as e:
                print(f"Error encrypting {file_path}: {e}")

def decrypt_directory(path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as file_to_decrypt:
                    encrypted_data = file_to_decrypt.read()
                decrypted_data = f.decrypt(encrypted_data)
                with open(file_path, "wb") as file_to_write:
                    file_to_write.write(decrypted_data)
            except (IOError, PermissionError) as e:
                print(f"Error decrypting {file_path}: {e}")
            except InvalidToken:
                print(f"Decryption failed for {file_path}: Invalid key or corrupted data")

# Main function
def main():
    # Check if a key file already exists
    try:
        key = load_key()
    except FileNotFoundError:
        key = generate_and_save_key()  # Generate and save a new key if it doesn't exist

    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a directory\n6. Decrypt a directory\n"))

    if mode == 1 or mode == 2:
        filepath = input("Enter the filepath: ")
        if mode == 1:
            encrypt_file(filepath, key)
            print("File encrypted.")
        elif mode == 2:
            decrypt_file(filepath, key)
            print("File decrypted.")
    elif mode == 3 or mode == 4:
        message = input("Enter the message: ")
        if mode == 3:
            encrypted = encrypt_message(message, key)
            if encrypted:
                print("Encrypted message:", encrypted)
        elif mode == 4:
            encrypted_message = input("Enter the encrypted message: ")
            decrypted = decrypt_message(encrypted_message.encode(), key)
            if decrypted:
                print("Decrypted message:", decrypted)
    elif mode == 5 or mode == 6:
        directory_path = input("Enter the directory path: ")
        if mode == 5:
            encrypt_directory(directory_path, key)
            print("Directory encrypted.")
        elif mode == 6:
            decrypt_directory(directory_path, key)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
           
