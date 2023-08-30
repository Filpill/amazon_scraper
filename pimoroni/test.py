import requests
from algoliasearch.search_client import SearchClient

# url = 'https://m00m3rfw1a-dsn.algolia.net/1/indexes/*/queries'
application_id = "M00M3RFW1A"
api_key = "97780d6ca6d719cafd5ef2556417e2ce"
client = SearchClient.create(application_id,api_key)
index = client.init_index('shop.pimoroni.com.variants')
results  = index.search('', {
                        # 'facetFilters': [
                        #     "collections:Raspberry Pi"
                        #     ],
                        'attributesToRetrieve': ["id","product_id","product_title"],
                    }
                )
print(results)
# r = requests.get(r"https://m00m3rfw1a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.5.1)%3B%20Browser%20(lite)&x-algolia-api-key=97780d6ca6d719cafd5ef2556417e2ce&x-algolia-application-id=M00M3RFW1A")
# print(r.text)

# curl 'https://m00m3rfw1a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.5.1)%3B%20Browser%20(lite)&x-algolia-api-key=97780d6ca6d719cafd5ef2556417e2ce&x-algolia-application-id=M00M3RFW1A' \
#   -H 'Accept: */*' \
#   -H 'Accept-Language: en-GB,en;q=0.9,en-US;q=0.8,bs;q=0.7,hr;q=0.6' \
#   -H 'Connection: keep-alive' \
#   -H 'Origin: https://shop.pimoroni.com' \
#   -H 'Referer: https://shop.pimoroni.com/' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: cross-site' \
#   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -H 'sec-ch-ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   --data-raw '{"requests":[{"indexName":"shop.pimoroni.com.variants","query":"","params":"facetFilters=%5B%5B%22collections%3ARaspberry%20Pi%22%5D%5D&hitsPerPage=32&page=0&attributesToRetrieve=%5B%22id%22%2C%22product_id%22%2C%22handle%22%2C%22retired%22%2C%22product_title%22%2C%22variant_title%22%2C%22description_first_paragraph%22%2C%22image%22%2C%22hidden_tags%22%2C%22price_ex_vat%22%2C%22compare_price_ex_vat%22%2C%22taxable%22%2C%22in_stock%22%2C%22rating%22%2C%22review_count%22%2C%22pre_order%22%2C%22special%22%5D"},{"indexName":"shop.pimoroni.com.variants","query":"","params":"facetFilters=%5B%5B%22collections%3ARaspberry%20Pi%22%5D%5D&hitsPerPage=0&maxValuesPerFacet=100&sortFacetValuesBy=count&facets=%5B%22special%22%2C%22tags%22%2C%22product_type%22%2C%22vendor%22%2C%22colour%22%2C%22region%22%5D"},{"indexName":"shop.pimoroni.com.variants","query":"","params":"facetFilters=%5B%5B%22collections%3ARaspberry%20Pi%22%5D%5D&hitsPerPage=0"}]}' \
#   --compressed