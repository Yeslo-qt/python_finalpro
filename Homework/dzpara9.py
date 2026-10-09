import requests
from bs4 import BeautifulSoup

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")

soup = BeautifulSoup(response.text, features="html.parser")

soup_list = soup.find_all("tr")

for elem in soup_list:
    if "USD" in elem.text:
        res = elem.find_all("td")
        rate = float(res[4].text.replace(",", "."))
        print("USD_rate::", rate)

        grn = float(input("Enter_UAH: "))
        usd = grn / rate

        print("USD amount:", round(usd, 2))
