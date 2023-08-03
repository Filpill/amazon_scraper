from playwright.sync_api import Playwright, sync_playwright, expect
from selectolax.parser import HTMLParser
from dataclasses import dataclass
from rich import print
import time
import csv

@dataclass
class Item:
    title: str
    price: str
    stock: str
    ratings: str

def get_html(page,current_url):
    page.goto(current_url)
    html = HTMLParser(page.content())
    return html

def parse_html(html):
    item = Item(
        title=html.css_first("h3").text(strip=True),
        price=html.css_first("span").text(strip=True),
        stock=html.css_first("span.stock-ok").text(strip=True),
        ratings=html.css_first("span").text(strip=True),
        )
    return item

def run(playwright: Playwright) -> None:
    # pw = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://shop.pimoroni.com/collections/raspberry-pi")
    # time.sleep(1)
    # page.get_by_role("link", name="Show more products…").click()
    # time.sleep(2)
    # page.get_by_role("link", name="Show more products…").click()
    current_url = page.url
    print(current_url)
    # html=get_html(page,current_url)
    # containers = page.query_selector_all('a.box'),
    # print(containers)
    # for c in containers:
    #     container_html = c. inner_html()
    #     item = parse_html(container_html)
    #     print(item)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
