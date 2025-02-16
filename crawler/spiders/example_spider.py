import requests
from bs4 import BeautifulSoup
from crawler.settings import HEADERS, TIMEOUT
from crawler.utils.logger import Logger

class ExampleSpider:
    def __init__(self):
        self.logger = Logger("example_spider")

    def fetch(self, url):
        """웹 페이지 요청 및 HTML 가져오기"""
        try:
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to fetch {url}: {e}")
            return None

    def parse(self, html):
        """HTML 데이터 파싱"""
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string if soup.title else "No Title"
        return {"title": title}

    def crawl(self):
        """크롤링 실행"""
        from crawler.urls import URLS

        for url in URLS:
            self.logger.info(f"Crawling {url}...")
            html = self.fetch(url)
            if html:
                data = self.parse(html)
                self.logger.info(f"Extracted Data: {data}")

if __name__ == "__main__":
    spider = ExampleSpider()
    spider.crawl()
