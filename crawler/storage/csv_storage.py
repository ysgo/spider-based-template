# 데이터 저장 모듈
import csv
import os

class CSVStorage:
    def __init__(self, filename="data/crawled_data.csv"):
        self.filename = filename
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    def save(self, data):
        """데이터를 CSV 파일에 저장"""
        with open(self.filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
