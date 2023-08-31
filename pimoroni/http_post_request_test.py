import requests
import json
import httpx
from urllib.parse import urlencode

application_id = "M00M3RFW1A"
api_key = "97780d6ca6d719cafd5ef2556417e2ce"
params = {
'x-algolia-agent': 'Algolia for JavaScript (4.5.1); Browser (lite)',
'x-algolia-api-key': api_key,
'x-algolia-application-id': application_id
}
search_data={"requests":[{"indexName":"shop.pimoroni.com.variants","query":"raspberry"}]}
# search_data={"requests":[{"indexName":"shop.pimoroni.com.variants","query":"raspberry","params":"facetFilters=%5B%5B%22collections%3ARaspberry%20Pi%22%5D%5D&hitsPerPage=16&page=0&attributesToRetrieve=%5B%22id%22%2C%22product_id%22%2C%22handle%22%2C%22retired%22%2C%22product_title%22%2C%22variant_title%22%2C%22description_first_paragraph%22%2C%22image%22%2C%22hidden_tags%22%2C%22price_ex_vat%22%2C%22compare_price_ex_vat%22%2C%22taxable%22%2C%22in_stock%22%2C%22rating%22%2C%22review_count%22%2C%22pre_order%22%2C%22special%22%5D"},{"indexName":"shop.pimoroni.com.variants","query":"","params":"facetFilters=%5B%5B%22collections%3ARaspberry%20Pi%22%5D%5D&hitsPerPage=0&maxValuesPerFacet=100&sortFacetValuesBy=count&facets=%5B%22special%22%2C%22tags%22%2C%22product_type%22%2C%22vendor%22%2C%22colour%22%2C%22region%22%5D"},{"indexName":"shop.pimoroni.com.variants","query":"","params":"facetFilters=%5B%5B%22collections%3ARaspberry%20Pi%22%5D%5D&hitsPerPage=0"}]}
search_url = 'https://m00m3rfw1a-dsn.algolia.net/1/indexes/*/queries?' + urlencode(params)
print(search_url)
response = httpx.post(search_url, json=search_data)
print(response.json())



# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
# 
# 
# data = {"requests":[{"indexName":"shop.pimoroni.com.variants","query":"","params":r"facetFilters: [[\"collections:Raspberry Pi\"]]"}]}
# jsondata = json.dumps(data)
# print(jsondata)
# 
# jsonObj = requests.post(url, data=jsondata, params=params).json()
# print(jsonObj)