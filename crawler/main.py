# 크롤러의 진입점(= 크롤러 실행 엔트리 포인트)
from crawler.spiders.example_spider import ExampleSpider

def run():
    spider = ExampleSpider()
    spider.crawl()

if __name__ == "__main__":
    run()