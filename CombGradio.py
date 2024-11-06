import asyncio
from playwright.async_api import async_playwright
import csv
import pandas as pd
import gradio as gr

async def check_elements1(page, selectors):
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
        item['site']="Amazon"

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
        item['site']="Amazon"

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
        item['site']="Amazon"

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

async def main1(user_input):
    modified_query = user_input.replace(" ", "+")
    url = "https://www.amazon.in/s?k=" + modified_query
    print("Amazon search URL:", url)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
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
        if await check_elements1(page, code1_selectors):
            product_data = await scrape_amazon_code1(page)
        elif await check_elements1(page, code3_selectors):
            product_data = await scrape_amazon_code3(page)
        else:
            print("No matching selectors found for Code 1 or Code 3.")

        with open('amazon_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['site','title', 'price', 'discount', 'image_url', 'url'])
            writer.writeheader()
            writer.writerows(product_data)

        print("Data saved to amazon_products.csv")
        await browser.close()


async def check_elements2(page, selectors):
    """Check if all selectors are present on the page."""
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
        item['site']="Flipkart"

        title_el = await product.query_selector('a.WKTcLC')
        item['title'] = await title_el.inner_text() if title_el else "N/A"

        price_el = await product.query_selector('div.Nx9bqj')
        item['price'] = await price_el.inner_text() if price_el else "N/A"

        discount_el = await product.query_selector('div.yRaY8j')
        if discount_el:
            full_text = await discount_el.inner_text()
            item['discount'] = full_text.split()[0] 
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
        item['site']="Flipkart"

        title_el = await product.query_selector('a.wjcEIp')
        item['title'] = await title_el.inner_text() if title_el else "N/A"

        price_el = await product.query_selector('div.Nx9bqj')
        item['price'] = await price_el.inner_text() if price_el else "N/A"

        discount_el = await product.query_selector('div.yRaY8j')
        if discount_el:
            full_text = await discount_el.inner_text()
            item['discount'] = full_text.split()[0]  
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
        item['site']="Flipkart"

        title_el = await product.query_selector('div.KzDlHZ')
        item['title'] = await title_el.inner_text() if title_el else "N/A"

        price_el = await product.query_selector('div.Nx9bqj')
        item['price'] = await price_el.inner_text() if price_el else "N/A"

        discount_el = await product.query_selector('div.yRaY8j')
        if discount_el:
            full_text = await discount_el.inner_text()
            item['discount'] = full_text.split()[0]  
        else:
            item['discount'] = "N/A"

        image_el = await product.query_selector('img.DByuf4')
        item['image_url'] = await image_el.get_attribute('src') if image_el else "N/A"

        link_el = await product.query_selector('a.CGtC98')
        relative_url = await link_el.get_attribute('href') if link_el else "N/A"
        item['url'] = f"https://www.flipkart.com{relative_url}" if relative_url else "N/A"

        product_data.append(item)

    return product_data


async def main2(user_input):
    modified_query = user_input.replace(" ", "+")
    url = "https://www.flipkart.com/search?q=" + modified_query
    print("Flipkart search URL:", url)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
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
        if await check_elements2(page, code1_selectors):
            product_data = await scrape_flipkart_code1(page)
        elif await check_elements2(page, code2_selectors):
            product_data = await scrape_flipkart_code2(page)
        elif await check_elements2(page, code3_selectors):
            product_data = await scrape_flipkart_code3(page)
        else:
            print("No matching selectors found for any of the codes.")

        with open('flipkart_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['site','title', 'price', 'discount', 'image_url', 'url'])
            writer.writeheader()
            writer.writerows(product_data)
        print("Data saved to flipkart_products.csv")
        await browser.close()

async def main(user_input):
    
    await main1(user_input)
    await asyncio.sleep(10)
    await main2(user_input)

    csv1 = pd.read_csv('amazon_products.csv')
    csv2 = pd.read_csv('flipkart_products.csv')
    combined_csv = pd.concat([csv1, csv2])
    combined_csv['price'] = combined_csv['price'].replace('[\₹,]', '', regex=True).astype(float)
    sorted_csv = combined_csv.sort_values(by='price')
    sorted_csv.to_csv('combined.csv', index=False)
    print("Combined and sorted CSV file saved as 'combined.csv'")

def display_combined_csv():
    combined_data = pd.read_csv('combined.csv')
    return combined_data

def generate_product_card(row):
    site=row['site']
    title = row['title']
    price = row['price']
    discount = row['discount']
    image_url = row['image_url']
    url = row['url']

    return f"""
    <div class="product-card">
        <img src="{image_url}" alt="{title}" class="product-image" />
        <h3 class="product-title">{title}</h3>
        <p class="product-price">Our Price ₹{price}</p>
        <p class="product-discount">Original {discount} </p>
        <a href="{url}" target="_blank" class="buy-button">Buy Now</a>
        <h3 class="product-title">{site}</h3>
    </div>
    """

def generate_product_cards():
    combined_data = display_combined_csv()
    cards_html = ''.join(combined_data.apply(generate_product_card, axis=1))
    return f"""
    <div class="product-grid">
        {cards_html}
    </div>
    """

def create_gradio_interface():
    user_input = gr.Textbox(label="Enter your search query", placeholder="Search for products")
    
    async def fetch_and_display_products(query):
        await main(query)
        return generate_product_cards()

    demo = gr.Interface(
        fn=fetch_and_display_products,
        inputs=user_input,
        outputs="html",
        title="ValueMart",
        description="Buy the cheapest/affordable product.",
        css="""
        .product-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }
        .product-card {
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 16px;
            width: 200px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .product-image {
            width: 100%;
            height: auto;
            margin-bottom: 8px;
        }
        .product-title {
            font-size: 16px;
            font-weight: bold;
            color: #333;
            margin: 8px 0;
        }
        .product-price {
            font-size: 18px;
            color: #007b00;
            margin: 4px 0;
        }
        .product-discount {
            font-size: 14px;
            color: #ff5722;
            margin: 4px 0;
        }
        .buy-button {
            display: inline-block;
            padding: 8px 16px;
            font-size: 14px;
            color: #fff;
            background-color: #007bff;
            border-radius: 4px;
            text-decoration: none;
            margin-top: 8px;
        }
        .buy-button:hover {
            background-color: #0056b3;
        }
        """
    )
    #demo.launch()
    demo.launch(server_name="0.0.0.0", server_port=7860)
create_gradio_interface()
