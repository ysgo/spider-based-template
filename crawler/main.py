# 크롤러의 진입점(= 크롤러 실행 엔트리 포인트)
from crawler.spiders.example_spider import ExampleSpider

def run():
    spider = ExampleSpider()
    spider.crawl()
    spider.scrape()
    spider.save_data()
    
    # 저장된 데이터 확인
    spider.load_data()
    
    # 파일 정리
    spider.cleanup_data()  # 30일 이상된 파일 삭제

if __name__ == "__main__":
    run()