import inspect
import requests
import math

print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))
print(inspect.getmodule(math.sqrt))

