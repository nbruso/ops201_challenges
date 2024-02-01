import pyzipper

filename = 'secret.txt'
zip_filename = 'secret_encrypted.zip'
password = '1234'

# First, create the secret.txt file with the message
with open(filename, 'w') as f:
    f.write("this is a secret message")

# Then, create an encrypted zip file containing the secret.txt file
with pyzipper.AESZipFile(zip_filename,'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(password.encode())
    zf.write(filename, arcname=filename)
