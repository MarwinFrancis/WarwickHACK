import requests


# price_list() takes 2 params and returns a list of dictionaries of top 5 search results
def price_list(query, country):
    headers = {"apikey": "522a97e0-79a2-11eb-a7a4-bf46803c6608"}

    params = (
       ("q", query),      #component model
       ("location","London,England,United Kingdom"),
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



