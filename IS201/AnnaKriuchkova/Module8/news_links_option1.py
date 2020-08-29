#import modules we will need for this task: BeautifulSoup & requests
from bs4 import BeautifulSoup
import requests

#define a link and store it in a variable 'link'
link = "https://news.ycombinator.com/news"

#using requests() method, extract link content and write it into an .html file
html_file = requests.get(link)
with open ('news.html', 'w') as file: 
    file.write(html_file.text) 

#initialize parsing
with open ("news.html") as parsing_file:
    beautifuls_parse = BeautifulSoup(parsing_file, features = "html.parser")

#create a for-loop that will find all news headers:\
#here we take beautifuls_parse variable, defined earlier, and apply to it .findall() method\
#with tag 'a' and class_ = 'storylink' as its arguments

for topic in beautifuls_parse.find_all('a', class_ = 'storylink'):
    print(topic.text) #prints each topic header
    print(topic['href']) #prints each topic link
    print()  #creates extra line of space between items
    file = open('news_data.txt', 'a') #create a .txt file that will append this data
    file.write(topic.text) #write  topic headers into the .txt file
    file.write(" \n")    #to create a new line
    file.write(topic['href']) #write topic links into the .txt file
    file.write(" \n") #to create a new line
    file.write(" \n") #to create an extra new line for separating entries
    file.close()  #close the file
