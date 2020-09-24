import bs4
import requests

file = requests.get('https://news.ycombinator.com/news')
lsoup = bs4.BeautifulSoup(file.text, 'html.parser')
elem=lsoup.find_all('a',class_='storylink')
print(elem)
url= 'https://news.ycombinator.com/news'










