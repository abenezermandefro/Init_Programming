from stegano import exifHeader as spec

msg = input("Enter a number to be hidden: ")

inImgJPG = 'image.jpg'

outImgJPG = 'image2.jpg'

spec.hide(inImgJPG, outImgJPG, msg)

message = spec.reveal(outImgJPG)
print(F'Reveal message: {message}')