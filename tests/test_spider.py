import unittest
from crawler.spiders.example_spider import ExampleSpider

class TestExampleSpider(unittest.TestCase):
    def setUp(self):
        self.spider = ExampleSpider()

    def test_fetch(self):
        url = "https://www.example.com"
        html = self.spider.fetch(url)
        self.assertIsNotNone(html, "Fetch failed: HTML should not be None")

    def test_parse(self):
        html = "<html><head><title>Test Page</title></head><body></body></html>"
        data = self.spider.parse(html)
        self.assertEqual(data["title"], "Test Page", "Parsing failed: Title mismatch")

if __name__ == "__main__":
    unittest.main()
