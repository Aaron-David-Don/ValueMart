#tries out all the possible tags present in different UI of amazon and get the info present inside them
import asyncio
from playwright.async_api import async_playwright
import csv

async def check_elements(page, selectors):
    for selector in selectors:
        if not await page.query_selector(selector):
            return False
    return True

async def scrape_flipkart_code1(page):
    print("Running Code 1")
    product_containers = await page.query_selector_all('div._1sdMkc.LFEi7Z')
    product_data = []

    for product in product_containers:
        item = {}

        title_el = await product.query_selector('a.WKTcLC')
        item['title'] = await title_el.inner_text() if title_el else "N/A"

        price_el = await product.query_selector('div.Nx9bqj')
        item['price'] = await price_el.inner_text() if price_el else "N/A"

        discount_el = await product.query_selector('div.yRaY8j')
        if discount_el:
            full_text = await discount_el.inner_text()
            item['discount'] = full_text.split()[0]  # Assuming discount is the first word
        else:
            item['discount'] = "N/A"

        
        image_el = await product.query_selector('img._53J4C-')
        item['image_url'] = await image_el.get_attribute('src') if image_el else "N/A"

      
        link_el = await product.query_selector('a.WKTcLC')
        relative_url = await link_el.get_attribute('href') if link_el else "N/A"
        item['url'] = f"https://www.flipkart.com{relative_url}" if relative_url else "N/A"

        product_data.append(item)

    return product_data

async def scrape_flipkart_code2(page):
    print("Running Code 2")
    product_elements = await page.query_selector_all('div.slAVV4')
    product_data = []

    for product in product_elements:
        item = {}

        
        title_el = await product.query_selector('a.wjcEIp')
        item['title'] = await title_el.inner_text() if title_el else "N/A"

        
        price_el = await product.query_selector('div.Nx9bqj')
        item['price'] = await price_el.inner_text() if price_el else "N/A"

        
        discount_el = await product.query_selector('div.yRaY8j')
        if discount_el:
            full_text = await discount_el.inner_text()
            item['discount'] = full_text.split()[0]  # Assuming discount is the first word
        else:
            item['discount'] = "N/A"

        
        image_el = await product.query_selector('img.DByuf4')
        item['image_url'] = await image_el.get_attribute('src') if image_el else "N/A"

        
        link_el = await product.query_selector('a.VJA3rP')
        relative_url = await link_el.get_attribute('href') if link_el else "N/A"
        item['url'] = f"https://www.flipkart.com{relative_url}" if relative_url else "N/A"

        product_data.append(item)

    return product_data

async def scrape_flipkart_code3(page):
    print("Running Code 3")
    product_elements = await page.query_selector_all('div.tUxRFH')
    product_data = []

    for product in product_elements:
        item = {}

        
        title_el = await product.query_selector('div.KzDlHZ')
        item['title'] = await title_el.inner_text() if title_el else "N/A"

        
        price_el = await product.query_selector('div.Nx9bqj')
        item['price'] = await price_el.inner_text() if price_el else "N/A"

        
        discount_el = await product.query_selector('div.yRaY8j')
        if discount_el:
            full_text = await discount_el.inner_text()
            item['discount'] = full_text.split()[0]  # Assuming discount is the first word
        else:
            item['discount'] = "N/A"

        
        image_el = await product.query_selector('img.DByuf4')
        item['image_url'] = await image_el.get_attribute('src') if image_el else "N/A"

        
        link_el = await product.query_selector('a.CGtC98')
        relative_url = await link_el.get_attribute('href') if link_el else "N/A"
        item['url'] = f"https://www.flipkart.com{relative_url}" if relative_url else "N/A"

        product_data.append(item)

    return product_data

async def main():
    user_input = input("Enter your search query: ")
    modified_query = user_input.replace(" ", "+")
    url = "https://www.flipkart.com/search?q=" + modified_query
    print("Flipkart search URL:", url)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_load_state('domcontentloaded')

        
        code1_selectors = [
            'div._1sdMkc.LFEi7Z',
            'a.WKTcLC',
            'div.Nx9bqj',
            'div.yRaY8j',
            'img._53J4C-',
            'a.WKTcLC'
        ]

        code2_selectors = [
            'div.slAVV4',
            'a.wjcEIp',
            'div.Nx9bqj',
            'div.yRaY8j',
            'img.DByuf4',
            'a.VJA3rP'
        ]

        code3_selectors = [
            'div.tUxRFH',
            'div.KzDlHZ',
            'div.Nx9bqj',
            'div.yRaY8j',
            'img.DByuf4',
            'a.CGtC98'
        ]

        
        product_data = []
        if await check_elements(page, code1_selectors):
            product_data = await scrape_flipkart_code1(page)
        elif await check_elements(page, code2_selectors):
            product_data = await scrape_flipkart_code2(page)
        elif await check_elements(page, code3_selectors):
            product_data = await scrape_flipkart_code3(page)
        else:
            print("No matching selectors found for any of the codes.")

        
        if product_data:
            with open('flipkart_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['title', 'price', 'discount', 'image_url', 'url'])
                writer.writeheader()
                writer.writerows(product_data)
            print("Data saved to flipkart_products.csv")

        await browser.close()

asyncio.run(main())
