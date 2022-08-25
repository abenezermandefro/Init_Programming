from stegano import lsb

secret_file_path = input("Enter the name of image with secret text inside: ")
secret_text = lsb.reveal(secret_file_path)
print(secret_text)