# Installing
# Install C++ Build Tools
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# python -m pip install cryptography
# Manually add  cryptography from Project Setting

# Import Library
import cryptography


# Getting a Key
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)

# Storing Keys
file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()

# Reading Keys
file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()
print(key)
print(key.decode('utf-8'))

# Creating User Defined Key
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password_provided = "password" # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes
salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
print(key)

# Encrypting
from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()
print(key)

message = "Kathmandu, Nepal".encode()
print(message)
f = Fernet(key)
encrypted = f.encrypt(message)
print(encrypted)

# Decrypting
encrypted = encrypted
f = Fernet(key)
decrypted = f.decrypt(encrypted)
print(decrypted)

#Encrypting and Decrypting Files

# Encrypting Files
from cryptography.fernet import Fernet
input_file = 'test.txt'
output_file = 'test.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)
print(encrypted)
with open(output_file, 'wb') as f:
    f.write(encrypted)

# Decrypting Files
from cryptography.fernet import Fernet
input_file = 'test.encrypted'
output_file = 'test.txt'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)
print(encrypted.decode())
with open(output_file, 'wb') as f:
    f.write(encrypted)
