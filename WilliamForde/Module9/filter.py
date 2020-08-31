from PIL import Image, ImageFilter

# blur image
img = Image.open('bulldog2.png')
im_blurred = img.filter(filter=ImageFilter.BLUR)
im_blurred.save('blur.png')

# greyscale
img_grey = img.convert('L')
img_grey.save('greyscale.png')