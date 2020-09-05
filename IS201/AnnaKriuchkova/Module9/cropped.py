from PIL import Image

catIm = Image.open('Zophie.png')

croppedIm = catIm.crop((335, 345, 565, 560))

croppedIm.save("cropped.png")

print(croppedIm.size)

