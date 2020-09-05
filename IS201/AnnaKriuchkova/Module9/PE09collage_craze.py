#import PIL module
from PIL import Image

#opening images to be used in a collage

img1 = Image.open('rose.png')
img2 = Image.open('jisoo.png')
img3 = Image.open('blackpink.png')
img4 = Image.open('bp_inyourarea.png')
img5 = Image.open('jennie.png')
img6 = Image.open('lisa.png')

#storing them in a list for convenience 
img_list = [img1, img2, img3, img4, img5, img6]

def create_collage_horizontally():
    """Create a function that connects several images horizontally"""
    #defining collage height
    #since we will be connecting images horizontally,\
    #we will take minimal height value out of all images \
    #in the list and adjust other images to it
    collage_height = min(im.height for im in img_list)
    #defining collage width
    #it should be a combined width of all available images
    collage_width = sum(im.width for im in img_list)
    #creating template onto which images will be pasted
    template = Image.new('RGB', (collage_width, collage_height), 'lavender')
    #setting starting value for width at 0
    position = 0 
    #creating a for-loop that will be adding images horizontally
    for im in img_list:
        template.paste(im, (position, 0))
        position += im.width
        #saving the result
        template.save('horizontal.png')

def create_collage_vertically():
    """Create a function that connects several images verically"""
    #defining collage width
    #since we will be connecting images vertically,\
    #we will take minimal width value out of all images \
    #in the list and adjust other images to it
    collage_width = min(im.width for im in img_list)
    #defining collage height
    #it should be a combined height of all available images
    collage_height = sum(im.height for im in img_list)
    #creating template onto which images will be pasted
    template = Image.new('RGB', (collage_width, collage_height), 'lavender')
    #setting starting value for height at 0
    position = 0 
    #creating a for-loop that will be connecting images vertically
    for im in img_list:
        template.paste(im, (0, position))
        position += im.height
        template.save('vertical.png')

def tiled():
    """Creating a function that resizes an image of choice
    and pastes it repatedly onto a template in a tiled manner"""

    #storing img4 width and height in separate variables
    width, height = img4.size
    #resizing img4 (6 times smaller than the original)
    resized = img4.resize((int(width//6), int(height//6)))
    #storing resized img4 width and height in separate variables
    width1, height1 = resized.size

    #creating a pattern onto which images will be pasted
    pattern = Image.new('RGBA', (600, 600), 'lavender')

    #storing pattern width and height in separate variables
    width2, height2= pattern.size
    
    #creating the for-loop that will handle the pasting
    for left in range (0, width2, width1):
        for top in range(0, height2, height1):
            pattern.paste(resized,(left, top))
    
    #saving the result
    pattern.save("blackpink_tiles.png")

#calling the functions
create_collage_horizontally()
create_collage_vertically()
tiled()