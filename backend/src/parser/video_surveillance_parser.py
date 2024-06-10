from backend.src.parser.main_parser import Parser

from urllib.parse import urljoin


class VideoSurveillanceParser:
    def __init__(self) -> None:
        self.base_url = 'https://www.farpost.ru'
        self.parser = Parser()

    async def get_page(self, url) -> str:
        return await self.parser.get_page(urljoin(self.base_url, url))

    async def get_links(self, page: str) -> list:
        return [link['href'] for link in
                (await self.parser.parse_data(page, 'a', 'bulletinLink bull-item__self-link auto-shy'))][:10]

    async def get_views(self, page: str) -> list:
        return [views.text for views in (await self.parser.parse_data(page, 'span', 'views nano-eye-text'))][:10]

    async def get_ad_header(self, page: str):
        return (await self.parser.parse_data(page, 'span', 'inplace auto-shy'))[0].text

    async def get_ad_author(self, page: str):
        return (await self.parser.parse_data(page, 'span', 'userNick auto-shy'))[0].find('a').text
