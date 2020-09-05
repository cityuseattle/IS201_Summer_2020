#import PIL
from PIL import Image

#open image to crop
dancer = Image.open('dancers.png')
#define area to crop 
#I used Paint to help identify coordinates 
cropped_area = (360, 8, 520, 240)
#store cropped image in a separate variable
cropped_dancer = dancer.crop(cropped_area)

#open background image, onto which\
#to paste cropped element
background = Image.open('monmartre.png')

#create a copy of background image to work with
background_copy = background.copy()
#paste cropped_dancer;
#again, used Paint to determine coordinates
background_copy.paste(cropped_dancer, (354, 196))
#save the result
background_copy.save('dancing_at_monmartre.png')
