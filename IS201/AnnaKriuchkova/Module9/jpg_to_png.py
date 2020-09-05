from PIL import Image

#Image info and changing format

#This returns value of img object data type

img = Image.open('bulldog.jpg')
width, height = img.size
print("Width:", width, "Height:", height)

#If .jpg file, change to .png
if img.format == 'JPEG':
    img.save('bulldog2.png')

