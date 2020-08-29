import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg112.txt')
res.raise_for_status() #always raise_for_status to ensure the file is downloadable; 
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

#this file is no longer accessible due to site maintenance on Gutenberg
