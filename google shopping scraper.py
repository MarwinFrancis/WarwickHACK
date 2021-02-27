import requests
import pprint

headers = {
  "apikey": "fa183bf0-7907-11eb-ae13-4f8f8bd5163d"}

params = (
   ("q", "RX 6800 XT"),
   ("tbm", "shop"),
   ("gl", "AT")
)

response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
pprint.pprint(response.json())
