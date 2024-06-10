import time

from bs4 import BeautifulSoup, ResultSet
from selenium import webdriver

from backend.src.core.settings import BASE_DIR


class Parser:
    async def get_page(self, url: str) -> str:
        chop = webdriver.ChromeOptions()
        chop.add_extension(f'{BASE_DIR}\utils\browser_extentions\CAPTCHA-Solver-hCAPTCHA-reCAPTCHA.crx')
        driver = webdriver.Chrome(options=chop)
        driver.get(url)
        time.sleep(5)
        html = driver.page_source
        driver.quit()

        return html

    async def parse_data(self, page: str, name: str, find_class: str) -> ResultSet:
        soup = BeautifulSoup(page, 'html.parser')
        data = soup.find_all(name, class_=find_class)

        return data
