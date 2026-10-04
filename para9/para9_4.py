import requests
res_parse_list = []
response = requests.get("https://coinmarketcap.com/")

# print(response.text)
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem in response_parse:
    if parse_elem.startswith("$"):
        for parse_elem_2 in parse_elem.split("</span>"):
          if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit() and not(parse_elem_2[-1].isalpha()):
              res_parse_list.append(parse_elem_2)

bitcoin_rate = res_parse_list[6]
print(bitcoin_rate)


