from PIL import Image
catIm = Image.open('zophie.png')

print(catIm.size) #privides image width and height
width, height = catIm.size #can also store these values in separate variables
print(width)
print(height)

print(catIm.filename) #to retrieve filename
print(catIm.format) #to retrieve image file format
print(catIm.format_description) #deciphers the file format abbreviation

catIm.save('zophie.jpg') #saving a copy of this image as a .jpg file

quartersizedIm = catIm.resize((int(width/2), int(height/2)))
quartersizedIm.save('quartersized.png')

tallIm = catIm.resize((width, height + 300))
tallIm.save('tallzophie.png')

catIm.rotate(90).save('rotated90.png')  #notice 'chain' method calls
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')

catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')

#mirroring horizontally versus vertically with .transpose() method
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')
