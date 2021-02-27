import requests
from pprint import pprint
import json

# price_list() takes 2 params and returns a list of dictionaries of top 5 search results
def price_list(query, country):
    headers = {"apikey": "fa183bf0-7907-11eb-ae13-4f8f8bd5163d"}

    params = (
       ("q", query),      #component model
       ("tbm", "shop"),
       ("gl", country)
    )
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result = response.json()
    top_five= []

    for i in result["shopping_results"][:5]:
        title = i["title"]
        price = i["price"]
        rev = i["reviews"]
        source = i["source"]

        temp = {'title': title,
                'price': price,
                'source': source,
                'reviews': rev
                }
        top_five.append(temp)

    return(top_five)



print(price_list("RX 6800 XT","AT"))
