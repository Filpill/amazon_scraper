from playwright.sync_api import Playwright, sync_playwright, expect
from selectolax.parser import HTMLParser
from dataclasses import dataclass
from rich import print
import time
import csv
import sys

@dataclass
class Item:
    title: str
    price: str
    rating: str
    stock: str

def get_html(page,current_url):
    page.goto(current_url)
    html = HTMLParser(page.content())
    return html

def parse_html(box_link):
    item = Item(
        title = box_link.css_first("h3").text(strip=True),
        price = box_link.css_first("span.price").text(strip=True),
        rating = box_link.css_first("span.rating").text(strip=True),
        stock = box_link.css_first("span.stock-ok").text(strip=True)
        )
    return item

def write_csv(product_list):
    with open(f'{sys.path[0]}\\products.csv','w', newline='') as output:
        field_names = ["title","price","rating","stock"]
        writer = csv.DictWriter(output,fieldnames=field_names)
        writer.writeheader()
        writer.writerows(product_list)

def run(playwright: Playwright) -> None:

    # Create Page and Navigate to URL
    scrape_url = "https://shop.pimoroni.com/collections/raspberry-pi"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(scrape_url)
    current_url = page.url

    # Pagination click through to load in other products
    page.locator("#collection").get_by_label("16\n            32\n            64\n          \n          per page").select_option("16")
    pages = 3
    for i in range(pages):
        page.get_by_role("link", name="Show more products…").click()
        page.mouse.wheel(0, 15000)
        time.sleep(3)

    # Parsing HTML on Page which contains product data 
    product_list = []
    html=get_html(page,current_url)
    box_links = html.css("a.box")

    # Loop through each product container and extract attributes
    for box_link in box_links:
        product = parse_html(box_link)
        product_list.append({
            'title':  product.title,
            'price':  product.price,
            'rating': product.rating,
            'stock':  product.stock
        })
    write_csv(product_list)

    # ---------------------
    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)