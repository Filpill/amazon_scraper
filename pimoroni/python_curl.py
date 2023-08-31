import json
import requests
import urllib.parse
import pandas as pd

base_url = 'https://m00m3rfw1a-dsn.algolia.net/1/indexes/*/queries'
params = {
    'x-algolia-agent': 'Algolia for JavaScript (4.5.1); Browser (lite)',
    'x-algolia-api-key': '97780d6ca6d719cafd5ef2556417e2ce',
    'x-algolia-application-id': 'M00M3RFW1A'
}

url = f"{base_url}?{urllib.parse.urlencode(params)}"

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,bs;q=0.7,hr;q=0.6',
    'Connection': 'keep-alive',
    'Origin': 'https://shop.pimoroni.com',
    'Referer': 'https://shop.pimoroni.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

attributes = [
              "id",
              "product_id",
              "handle",
              "retired",
              "product_title",
              "variant_title",
              "description_first_paragraph",
              "image",
              "hidden_tags",
              "price_ex_vat",
              "compare_price_ex_vat",
              "taxable",
              "in_stock",
              "rating",
              "review_count",
              "pre_order",
              "special"
              ]

hits = 32

data = {
    'requests': [
        {
            'indexName': 'shop.pimoroni.com.variants',
            'query': '',
            'params': f'facetFilters=[["collections:Raspberry Pi"]]&hitsPerPage={hits}&page=0&attributesToRetrieve={attributes}'
        }
    ]
}

response = requests.post(url, json=data, headers=headers)
print(response.text)

df_pi = pd.DataFrame.from_dict(response)
print(df_pi)