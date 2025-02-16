# API 크롤러
import requests
from crawler.settings import HEADERS
from crawler.utils.logger import Logger

class APISpider:
    def __init__(self, api_url):
        self.api_url = api_url
        self.logger = Logger("api_spider")

    def fetch_data(self):
        """API에서 데이터 가져오기"""
        try:
            response = requests.get(self.api_url, headers=HEADERS)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"API Request failed: {e}")
            return None

if __name__ == "__main__":
    api_spider = APISpider("https://jsonplaceholder.typicode.com/posts")
    data = api_spider.fetch_data()
    if data:
        print(data[:3])  # 첫 3개 데이터 출력
