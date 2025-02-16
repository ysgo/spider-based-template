# 중복 요청 방지
class Cache:
    """이미 크롤링한 URL을 저장하여 중복 요청 방지"""
    def __init__(self):
        self.visited_urls = set()

    def is_cached(self, url):
        return url in self.visited_urls

    def add(self, url):
        self.visited_urls.add(url)
