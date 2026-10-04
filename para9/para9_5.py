import requests
from bs4 import BeautifulSoup

response = requests.get("https://coinmarketcap.com/")
soup = BeautifulSoup(response.text, features="html.parser")
soup_list = soup.find_all("div", {"class": "sc-664711f9-0 kXPUOA"})
# for elem in soup_list:
#     print(elem)
res = soup_list[1].find("span")
print(res.text)