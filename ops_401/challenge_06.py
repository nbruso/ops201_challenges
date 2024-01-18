# OPS401D10  Ops Challenge 06
# 01/16/2024
# Dominique Bruso
# source:https://pypi.org/project/cryptography/; https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python' https://chat.openai.com/share/c4d71d63-6af1-4ee4-a196-cce4e9491a83

from cryptography.fernet import Fernet

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
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# Function to encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

# Main function
def main():
    # Check if a key file already exists
    try:
        key = load_key()
    except FileNotFoundError:
        key = generate_and_save_key()  # Generate and save a new key if it doesn't exist

    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n"))

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
            print("Encrypted message:", encrypted)
        elif mode == 4:
            decrypted = decrypt_message(message, key)
            print("Decrypted message:", decrypted)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
