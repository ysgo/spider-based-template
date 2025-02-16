# 크롤러(스파이더) 패키지 초기화 (ExampleSpider 클래스를 패키지에서 바로 가져올 수 있도록 설정합니다.)
from crawler.spiders import ExampleSpider

spider = ExampleSpider()

def get_spider():
    from crawler.spiders.example_spider import ExampleSpider
    return ExampleSpider()
