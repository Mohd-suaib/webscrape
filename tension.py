import requests
from bs4 import BeautifulSoup
req=requests.get("https://www.stfrancismedicalcenter.com/find-a-provider/")

# soup=BeautifulSoup(req.content,"html.parser")
# print(soup.prettify())
# print(soup.get_text())
# res=soup.title
# print(res.prettify())
# print(res.get_text())

# classes = soup.find_all("div", class_="class-name")
# for class_info in classes:
#     print(class_info.text)