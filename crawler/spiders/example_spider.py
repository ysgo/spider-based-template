import requests
from bs4 import BeautifulSoup
from crawler.settings import HEADERS, TIMEOUT
from crawler.utils.logger import Logger
from utils.file_manager import FileManager

class ExampleSpider:
    def __init__(self):
        self.logger = Logger("example_spider")
        self.file_manager = FileManager()
        self.data = []  # 크롤링 데이터 저장

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
                
    def scrape(self):
        """샘플 크롤링 데이터"""
        self.data = [
            {"title": "데이터 1", "url": "https://example.com/1"},
            {"title": "데이터 2", "url": "https://example.com/2"}
        ]
        print("🕷 크롤링 완료!")
        
    def save_data(self):
        """크롤링 데이터를 JSON 파일로 저장"""
        if not self.data:
            print("⚠️ 저장할 데이터가 없습니다.")
            return

        self.file_manager.save_json("crawl_results", self.data)

    def load_data(self):
        """저장된 데이터 불러오기"""
        data = self.file_manager.load_json("crawl_results")
        if data:
            print("📂 불러온 데이터:", data)
    
    def cleanup_data(self):
        """파일 정리 작업"""
        self.file_manager.cleanup_files()

if __name__ == "__main__":
    spider = ExampleSpider()
    spider.crawl()
