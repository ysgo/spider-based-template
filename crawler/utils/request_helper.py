import requests
from crawler.settings import HEADERS, TIMEOUT

def fetch_html(url):
    """웹 페이지 HTML 가져오기"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
