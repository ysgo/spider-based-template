# 설정 관련 모듈
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
TIMEOUT = 10  # 요청 타임아웃 (초)
HEADERS = {
    "User-Agent": USER_AGENT
}
RETRY_COUNT = 3  # 요청 재시도 횟수