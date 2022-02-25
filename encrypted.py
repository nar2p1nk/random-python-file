from cryptography.fernet import Fernet

key = Fernet.generate_key()

fkey = Fernet(key)

def encrypt(password):
    encryptedPassword = fkey.encrypt(password.encode())
    # print(encryptedPassword)

def decrypt(encryption):
    decryptedPassword=fkey.decrypt(encryptedPassword).decode()
    print(decryptedPassword)