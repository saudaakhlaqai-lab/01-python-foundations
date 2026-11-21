import json
from urllib.request import urlopen

url = "https://api.github.com"
with urlopen(url) as response:
	print(response.status)
	print(json.loads(response.read()))