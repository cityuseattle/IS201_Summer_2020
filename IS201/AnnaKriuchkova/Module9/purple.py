from PIL import Image

im = Image.new('RGBA', (100, 200), 'purple')
#arguments that .new() function accepts: \
#'RGBA' (to set a color mode); \
# two-integer tuple for image width and height
# background color

im.save('purpleImage.png')

im2 = Image.new('RGBA', (20, 20))
#note that invisible black (0,0,0,0) is used as a default, \
#if no color argument is passed

im2.save('transparentImage.png')

