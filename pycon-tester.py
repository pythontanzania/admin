import requests
import json

urk = "http://pycon.fuadhabib.xyz/api/speakers/"

response = requests.get(urk)

unformatted = response.json()

forty = json.dumps(unformatted, indent=2)


print(forty)
