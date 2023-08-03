import requests
from json import loads

url = 'https://m00m3rfw1a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.5.1)%3B%20Browser%20(lite)&x-algolia-api-key=97780d6ca6d719cafd5ef2556417e2ce&x-algolia-application-id=M00M3RFW1A'
response = requests.get(url)
print(response.status_code)
data = loads(response.text)