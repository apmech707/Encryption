'''This is a program that encrypts a file using the cryptography.fernet module.
It is a command line interface app.'''

from cryptography.fernet import Fernet

def main():
    path = input("Full path name of file to encrypt. \n")
    print("If you already have a key enter it now. Otherwise press Enter.")
    answer = input()

    if len(answer) == 0:
        key = Fernet.generate_key()
        print("Save this key or else.")
        key = key.decode()
        print(key)
    elif len(answer) > 0:
        key = answer
    
    key = key.encode()
    fernet = Fernet(key)

    def encrypt_file(path):
        with open(path, "rb") as f:
            file_as_bytes = f.read()

        encrypted_file = fernet.encrypt(file_as_bytes)

        with open(path, "wb") as f:
            f.write(encrypted_file)


    encrypt_file(path)

    print("Finished. Your file has been encrypted")
    exit()

while True:
    try:
        main()
    except Exception as e:
        print("There was a problem.")
        print(repr(e))
        print("Ignore the previous key. We'll try that again.\n")

