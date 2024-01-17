# OPS401D10  Ops Challenge 06
# 01/16/2024
# Dominique Bruso
# source:https://pypi.org/project/cryptography/; https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python' https://chat.openai.com/share/c4d71d63-6af1-4ee4-a196-cce4e9491a83

from cryptography.fernet import Fernet

# Function to generate a secret key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a file
def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file: # Open the file to read data in binary mode
        file_data = file.read() # Read the file data
    encrypted_data = f.encrypt(file_data) # Encrypt the file data
    with open(filename, "wb") as file: # Open the file to write data in binary mode
        file.write(encrypted_data) # Write the encrypted data back to the file

# Function to decrypt a file
def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file: # Open the file to read encrypted data in binary mode
        encrypted_data = file.read() # Read the encrypted file data
    decrypted_data = f.decrypt(encrypted_data) # Decrypt the file data
    with open(filename, "wb") as file: # Open the file to write decrypted data in binary mode
        file.write(decrypted_data) # Write the decrypted data back to the file

# Function to encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode()) # Encrypts and returns the encoded message

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode() # Decrypts and decodes the message back to string

# Main function
def main():
    key = generate_key() # Generate an encryption key

    # Ask the user to select a mode
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n"))

    # Handle file encryption/decryption
    if mode == 1 or mode == 2:
        filepath = input("Enter the filepath: ") # Get the file path from the user
        if mode == 1:
            encrypt_file(filepath, key) # Encrypt the file
            print("File encrypted.")
        elif mode == 2:
            decrypt_file(filepath, key) # Decrypt the file
            print("File decrypted.")

    # Handle message encryption/decryption
    elif mode == 3 or mode == 4:
        message = input("Enter the message: ") # Get the message from the user
        if mode == 3:
            encrypted = encrypt_message(message, key) # Encrypt the message
            print("Encrypted message:", encrypted)
        elif mode == 4:
            decrypted = decrypt_message(message, key) # Decrypt the message
            print("Decrypted message:", decrypted)

    else:
        print("Invalid mode selected.")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()

