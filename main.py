import aiohttp
import asyncio
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_options = Options()
chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4147.125 Safari/537.36")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# browser.implicitly_wait(5)

with open('link.txt','r',encoding='utf-8') as f:
    main_url = f.readline().strip()

# target_links = []
for i in range(50000):
    browser = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options)
    browser.get(main_url)
    sleep(3)
    browser.close()
    print(i)
# all_blocks = browser.find_elements_by_xpath("//div[@id='catalog-content']//div[@class='product-card-overflow']//div")
# for block in all_blocks:
#     if 'j-advert-card-item advert-card-item' in block.get_attribute('class'):
#         target_links.append(f"https://www.wildberries.ru/catalog/{block.get_attribute('data-popup-nm-id')}/detail.aspx?targetUrl=XS")

# async def main(link):
#     async with aiohttp.ClientSession() as session:
#         await session.get(link)
        # async with session.get(link) as resp:
        #     page = await resp.text()
        #     print(page)

# for link in target_links:
#     for i in range(5000):
#         asyncio.run_until_complete(main(link))
#         print(i)
