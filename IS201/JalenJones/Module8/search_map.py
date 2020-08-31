import webbrowser
import sys

place='city university of seattle'
if len(sys.argv)>1:
    #Get address from command line
    place=''.join(sys.argv[1:])

webbrowser.open("https://google.com/maps/search/"+place)