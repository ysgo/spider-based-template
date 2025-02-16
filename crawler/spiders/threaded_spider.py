# 멀티스레드 크롤러
import threading
import requests
from bs4 import BeautifulSoup
from crawler.settings import HEADERS, TIMEOUT
from crawler.utils.logger import Logger
from crawler.utils.cache import Cache

class ThreadedSpider:
    def __init__(self, urls):
        self.urls = urls
        self.logger = Logger("threaded_spider")
        self.cache = Cache()

    def fetch(self, url):
        """웹 페이지 요청"""
        if self.cache.is_cached(url):
            self.logger.info(f"Skipping {url} (already crawled)")
            return None
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()
            self.cache.add(url)
            return response.text
        except requests.RequestException as e:
            self.logger.error(f"Failed to fetch {url}: {e}")
            return None

    def parse(self, html):
        """HTML 데이터 파싱"""
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string if soup.title else "No Title"
        return {"title": title}

    def crawl(self, url):
        """단일 URL 크롤링"""
        self.logger.info(f"Crawling {url}...")
        html = self.fetch(url)
        if html:
            data = self.parse(html)
            self.logger.info(f"Extracted Data: {data}")

    def run(self):
        """멀티스레드 실행"""
        threads = []
        for url in self.urls:
            thread = threading.Thread(target=self.crawl, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    from crawler.urls import URLS
    spider = ThreadedSpider(URLS)
    spider.run()