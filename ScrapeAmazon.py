#tries out all the possible tags present in different UI of amazon and get the info present inside them
import asyncio
from playwright.async_api import async_playwright
import csv

async def check_elements(page, selectors):
    """Check if all selectors are present on the page."""
    for selector in selectors:
        if not await page.query_selector(selector):
            return False
    return True

async def scrape_amazon_code1(page):
    print("Running Code 1")
    products = await page.query_selector_all('div.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20')
    product_data = []

    for product in products:
        item = {}

        title_el = await product.query_selector('span.a-size-base-plus.a-color-base.a-text-normal')
        item['title'] = await title_el.inner_text() if title_el else "N/A"

        price_el = await product.query_selector('span.a-offscreen')
        item['price'] = await price_el.inner_text() if price_el else "N/A"

        discount_el = await product.query_selector('span.a-price.a-text-price span.a-offscreen')
        item['discount'] = await discount_el.inner_text() if discount_el else "N/A"

        image_el = await product.query_selector('img.s-image')
        item['image_url'] = await image_el.get_attribute('src') if image_el else "N/A"

        link_el = await product.query_selector('a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')
        relative_url = await link_el.get_attribute('href') if link_el else "N/A"
        item['url'] = f"https://www.amazon.in{relative_url}" if relative_url else "N/A"

        product_data.append(item)

    return product_data

async def scrape_amazon_code2(page):
    print("Running Code 2")
    products = await page.query_selector_all('div.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20')
    product_data = []

    for product in products:
        item = {}

        title_el = await product.query_selector('span.a-size-base-plus.a-color-base.a-text-normal')
        item['title'] = await title_el.inner_text() if title_el else "N/A"

        price_el = await product.query_selector('span.a-offscreen')
        item['price'] = await price_el.inner_text() if price_el else "N/A"

        discount_el = await product.query_selector('span.a-price.a-text-price span.a-offscreen')
        item['discount'] = await discount_el.inner_text() if discount_el else "N/A"

        image_el = await product.query_selector('img.s-image')
        item['image_url'] = await image_el.get_attribute('src') if image_el else "N/A"

        link_el = await product.query_selector('a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')
        relative_url = await link_el.get_attribute('href') if link_el else "N/A"
        item['url'] = f"https://www.amazon.in{relative_url}" if relative_url else "N/A"

        product_data.append(item)

    return product_data

async def scrape_amazon_code3(page):
    print("Running Code 3")
    products = await page.query_selector_all('div.sg-col-20-of-24.s-result-item.s-asin.sg-col-0-of-12.sg-col-16-of-20.sg-col.s-widget-spacing-small.sg-col-12-of-16')
    product_data = []

    for product in products:
        item = {}

        title_el = await product.query_selector('span.a-size-medium.a-color-base.a-text-normal')
        item['title'] = await title_el.inner_text() if title_el else "N/A"

        price_el = await product.query_selector('span.a-offscreen')
        item['price'] = await price_el.inner_text() if price_el else "N/A"

        discount_el = await product.query_selector('span.a-price.a-text-price span.a-offscreen')
        item['discount'] = await discount_el.inner_text() if discount_el else "N/A"

        image_el = await product.query_selector('img.s-image')
        item['image_url'] = await image_el.get_attribute('src') if image_el else "N/A"

        link_el = await product.query_selector('a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')
        relative_url = await link_el.get_attribute('href') if link_el else "N/A"
        item['url'] = f"https://www.amazon.in{relative_url}" if relative_url else "N/A"

        product_data.append(item)

    return product_data

async def main():
    user_input = input("Enter your search query: ")
    modified_query = user_input.replace(" ", "+")
    url = "https://www.amazon.in/s?k=" + modified_query
    print("Amazon search URL:", url)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_load_state('domcontentloaded')

        code1_selectors = [
            'div.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20',
            'span.a-size-base-plus.a-color-base.a-text-normal',
            'span.a-offscreen',
            'span.a-price.a-text-price span.a-offscreen',
            'img.s-image',
            'a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal'
        ]
        code3_selectors = [
            'div.sg-col-20-of-24.s-result-item.s-asin.sg-col-0-of-12.sg-col-16-of-20.sg-col.s-widget-spacing-small.sg-col-12-of-16',
            'span.a-size-medium.a-color-base.a-text-normal',
            'span.a-offscreen',
            'span.a-price.a-text-price span.a-offscreen',
            'img.s-image',
            'a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal'
        ]

        product_data = []
        if await check_elements(page, code1_selectors):
            product_data = await scrape_amazon_code1(page)
        elif await check_elements(page, code3_selectors):
            product_data = await scrape_amazon_code3(page)
        else:
            print("No matching selectors found for Code 1 or Code 3.")

        with open('amazon_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['title', 'price', 'discount', 'image_url', 'url'])
            writer.writeheader()
            writer.writerows(product_data)

        print("Data saved to amazon_products.csv")
        await browser.close()

asyncio.run(main())
