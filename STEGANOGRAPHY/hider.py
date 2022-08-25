from stegano import lsb


text = input("Please enter a text to be embeded: ")
secret = lsb.hide('image.png', text)
secret.save('new-secret-image.png')