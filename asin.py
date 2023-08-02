import csv
from playwright.sync_api import sync_playwright

def get_asin(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

        # Get all links containing ASINs
        asin_list = []
        links = page.query_selector_all('a')
        for link in links:
            href = link.get_attribute('href')
            if href is not None:
                if '/dp' in href:
                    split_url = href.split('/')
                    asin_index = split_url.index('dp') + 1
                    asin = split_url[asin_index][0:10]
                    asin_list.append(asin)
        browser.close()
        return list(set(asin_list))

def append_csv(asin_list):
    with open('asin.csv','a+', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(asin_list)

def main():
    url = 'https://www.amazon.com/deals'
    asin_list = get_asin(url)
    append_csv(asin_list)

if __name__ == "__main__":
    main()