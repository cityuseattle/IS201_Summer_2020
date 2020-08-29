import webbrowser    #module for opening URLs in a browser
import sys           #module for analyzing the environment in which program runs

place = 'City University of Seattle'
if len(sys.argv) > 1:                #len(sys,argv) - for the number of arguments
    #Get address from command line
    place = ''.join(sys.argv[1:])

webbrowser.open('https://google.com/maps/search/' + place)