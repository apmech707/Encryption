'''This is a program that decrypts a file using that has been encrypted with 
the cryptography.fernet module. It is a command line interface app.'''

from cryptography.fernet import Fernet

def main():
    print("Which file do you need to decrypt?\nEnter full path name.")
    path = input()
    print("Enter key to decrypt file.")
    key = input()
    key = key.encode()
    fernet = Fernet(key)

    def decrypt_file(path):
        with open(path, "rb") as f:
            file_as_bytes = f.read()

        decrypted_file = fernet.decrypt(file_as_bytes)

        with open(path, "wb") as f:
            f.write(decrypted_file)
        
        print("Finished. Your file has been decrypted.")

        exit()

    decrypt_file(path)

while True:
    try:
        main()
    except Exception:
        print("There was a problem. Let's try again.")
