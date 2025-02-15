from bs4 import BeautifulSoup

def extract_data(html):
    """HTML에서 특정 데이터 추출"""
    soup = BeautifulSoup(html, "html.parser")
    data = {
        "title": soup.title.string if soup.title else "No Title",
        "headings": [h.get_text() for h in soup.find_all("h1")],
    }
    return data
