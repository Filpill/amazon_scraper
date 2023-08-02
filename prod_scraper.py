from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from dataclasses import dataclass
from rich import print
import time
import csv


@dataclass
class Item:
    asin: str
    title: str
    price: str

def get_html(page, asin):
    url = f"https://amazon.co.uk/dp/{asin}"
    page.goto(url)
    html = HTMLParser(page.content())
    return html

def parse_html(html, asin):
    try:
        item = Item(
            asin=asin,
            title=html.css_first("span#productTitle").text(strip=True),
            price=html.css_first("span.a-offscreen").text(strip=True)
        )
        return item
    except:
        print(f'{asin} parsing html failed trying the h1 tag')
        item = Item(
            asin=asin,                                                         
            title=html.css_first("h1").text(strip=True),
            price=''
        )
        return item

def read_csv(filename):
    with open(filename,'r') as f:
        reader = csv.reader(f)
        asin_list = [asin for asin in reader][0]
        return asin_list

def run(asin):
    pw = sync_playwright().start()
    browser = pw.chromium.launch()
    page = browser.new_page()
    html = get_html(page, asin)
    product = parse_html(html, asin)
    print(product)
    browser.close()
    pw.stop()

def main():
    asin_list = read_csv('asin.csv')
    for asin in asin_list:
        run(asin)

if __name__ == "__main__":
    main()