import requests
from bs4 import BeautifulSoup as bs


page = requests.get('https://www.youtube.com/watch?v=7bE2mI4ePeU&feature=emb_logo')
soup = bs(page.content, 'html.parser')

print(soup.prettify())