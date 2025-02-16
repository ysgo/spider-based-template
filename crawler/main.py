# 크롤러의 진입점(= 크롤러 실행 엔트리 포인트)
from crawler.spiders.example_spider import ExampleSpider

def run():
    spider = ExampleSpider()
    spider.crawl()
    spider.scrape()
    spider.save_data()
    
    # 저장된 데이터 확인
    spider.load_data()
    
    # 파일 정리 및 삭제 기록 (자동으로 수행됨)
    # spider.cleanup_data()  # 직접 호출할 필요 없음, 자동으로 실행됨

if __name__ == "__main__":
    run()