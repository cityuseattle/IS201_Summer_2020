import bs4
import requests

file = open('C:\\Users\\AnnaK\\IS201_Summer_2020\\IS201\\AnnaKriuchkova\\Module8\\example.html')
lsoup = bs4.BeautifulSoup(file.read(), "html.parser")
elem = lsoup.select("#author")
print(elem[0].get_text())

res = requests.get("http://www.cs.cmu.edu/~pausch/")
#used to display error message, if url is not valid
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
#store a list of all <h1> tags to element
element = soup.select("h1")
for item in element:
    print(item)
    print(item.get_text())
    print()

#print(soup.prettify())
