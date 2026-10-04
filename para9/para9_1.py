import urllib.request

opener = urllib.request.build_opener()
respounse = opener.open("https://httpbin.org/get")
print(respounse.read())

