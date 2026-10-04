import requests

response = requests.post("https://httpbin.org/post",
                         "test data", headers={"h1": "Test title"})
print(response.text)
