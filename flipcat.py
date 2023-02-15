import pandas as pd
import requests
from bs4 import BeautifulSoup

url="https://www.flipkart.com/search?q=mobile+under+15000+rs&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_12_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_12_na_na_na&as-pos=3&as-type=RECENT&suggestionId=mobile+under+15000+rs&requestId=f1b2423e-246a-4775-bcc4-6ccd7d525cc8&as-searchtext=mobile%20under"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
# print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
for link in soup.find_all('a'):
    print(link.get('href'))
# print(soup.get_text())
for img in soup.find_all('img'):
    print(img.get('src'))