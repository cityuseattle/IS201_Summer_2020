from PIL import ImageColor
#note the import format above! 

print(ImageColor.getcolor("red", "RGBA"))
print(ImageColor.getcolor('Black', 'RGBA'))
print(ImageColor.getcolor('blue', 'RGBA'))
print(ImageColor.getcolor('darkblue', 'RGBA'))
print(ImageColor.getcolor('chocolate', 'RGBA'))
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))
print(ImageColor.getcolor('purple', 'RGBA'))
print(ImageColor.getcolor('orchid', 'RGBA'))
print(ImageColor.getcolor('sienna', 'RGBA'))

#full list of acceptable color arguments
import webbrowser
webbrowser.open('en.wikipedia.org/wiki/Web_colors')