#importing BeautifulSoup & requests modules
from bs4 import BeautifulSoup
import requests
import openpyxl
from openpyxl.styles import Font, Alignment

#downloading the link as an html-text that maey be displayed in our terminal
source = requests.get("https://news.ycombinator.com/news").text 

#create and format an excel spreadsheet, which will record our final output
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "News"
sheet['A1'] = "News Headers"
sheet['B1'] = "Link"
sheet['A1'].font = Font(name="Times New Roman", bold=True)
sheet['A1'].alignment = Alignment(horizontal='center')
sheet['B1'].font = Font(name="Times New Roman", bold=True)
sheet['B1'].alignment = Alignment(horizontal='center')
sheet.column_dimensions['A'].width = 78
sheet.column_dimensions['B'].width = 150

#initialize parsing
parse_link = BeautifulSoup(source, features="html.parser")

#print(parse_link.prettify()) #allows to see us in a terminal what website page looks like \
#as a properly indented html text (if we remove comment symbol)

#create a for-loop that finds all news headers:\
#note that we pass tag 'a' and class_ = "storylink" as .find_all() method's arguments

for topic in parse_link.find_all('a',class_ = "storylink"):
    print(topic.text)    #prints each topic header
    print(topic['href']) #prints each topic link
    print()   #creates extra line of space between items
    news_data = [(topic.text, topic['href'])] #creates a list object which stores data in a specific format
    for news in news_data:
        sheet.append(news)    #append to the spreadsheet

#save spreadsheet with data
wb.save("news_data.xlsx")
