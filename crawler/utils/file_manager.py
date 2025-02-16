# 파일 저장 및 로드 기능 추가
import os
import json
import time
import schedule
import threading
from datetime import datetime

class FileManager:
    """크롤링 데이터를 저장 및 로드하는 파일 관리 클래스"""

    def __init__(self, base_dir="data", cleanup_days=30, log_file="deleted_files_log.json"):
        self.base_dir = base_dir
        self.cleanup_days = cleanup_days  # 정리할 기준 날짜 (예: 30일)
        self.log_file = log_file  # 삭제된 파일 로그 파일
        os.makedirs(self.base_dir, exist_ok=True)  # 기본 저장 폴더 생성
        self.deleted_files = self.load_deleted_files_log()  # 이전 삭제 기록 불러오기

    def _get_date_folder(self):
        """현재 날짜별 폴더를 반환 (예: 2025-02-16)"""
        return datetime.now().strftime("%Y-%m-%d")
    
    def save_json(self, filename, data):
        """데이터를 JSON 파일로 저장"""
        file_path = os.path.join(self.base_dir, f"{filename}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ 파일 저장 완료: {file_path}")
        
    def load_json(self, filename):
        """JSON 파일을 불러오기"""
        file_path = os.path.join(self.base_dir, f"{filename}.json")
        if not os.path.exists(file_path):
            print(f"⚠️ 파일이 존재하지 않습니다: {file_path}")
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_files(self):
        """저장된 파일 목록 확인"""
        return [f for f in os.listdir(self.base_dir) if f.endswith(".json")]
    
    def save_json_date_dirs(self, filename, data):
        """데이터를 JSON 파일로 날짜별 폴더에 저장"""
        date_folder = self._get_date_folder()
        folder_path = os.path.join(self.base_dir, date_folder)
        os.makedirs(folder_path, exist_ok=True)  # 날짜별 폴더 생성

        file_path = os.path.join(folder_path, f"{filename}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ 파일 저장 완료: {file_path}")

    def load_json_date_dirs(self, filename):
        """특정 날짜 폴더에서 JSON 파일을 불러오기"""
        date_folder = self._get_date_folder()
        file_path = os.path.join(self.base_dir, date_folder, f"{filename}.json")

        if not os.path.exists(file_path):
            print(f"⚠️ 파일이 존재하지 않습니다: {file_path}")
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_files_date_dirs(self):
        """저장된 파일 목록 확인 (날짜별 폴더 내)"""
        files = []
        for date_folder in os.listdir(self.base_dir):
            folder_path = os.path.join(self.base_dir, date_folder)
            if os.path.isdir(folder_path):
                files.extend(
                    os.path.join(date_folder, f)
                    for f in os.listdir(folder_path)
                    if f.endswith(".json")
                )
        return files
    
    def cleanup_files(self):
        """지정된 기간 이상된 파일을 찾아 삭제하는 메서드"""
        """지정된 기간(예: 30일) 이상된 파일을 삭제"""
        current_time = time.time()
        deleted_files = []

        for date_folder in os.listdir(self.base_dir):
            folder_path = os.path.join(self.base_dir, date_folder)
            if os.path.isdir(folder_path):
                for filename in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, filename)
                    if filename.endswith(".json"):
                        file_mtime = os.path.getmtime(file_path)  # 파일 마지막 수정 시간
                        file_age = current_time - file_mtime

                        # 지정된 기간 이상된 파일 삭제
                        if file_age > self.cleanup_days * 86400:  # 86400초 = 1일
                            os.remove(file_path)
                            deleted_files.append(file_path)

        if deleted_files:
            print(f"🗑 삭제된 파일: {', '.join(deleted_files)}")
            self.log_deleted_files(deleted_files)
        else:
            print("⚠️ 삭제할 파일이 없습니다.")

    def log_deleted_files(self, deleted_files):
        """삭제된 파일 목록을 로그 파일에 기록"""
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "deleted_files": deleted_files
        }

        self.deleted_files.append(log_entry)
        self.save_deleted_files_log()

    def save_deleted_files_log(self):
        """삭제된 파일 로그를 파일에 저장"""
        with open(self.log_file, "w", encoding="utf-8") as log_file:
            json.dump(self.deleted_files, log_file, ensure_ascii=False, indent=4)
        print(f"📜 삭제 기록이 {self.log_file}에 저장되었습니다.")

    def load_deleted_files_log(self):
        """이전 삭제 기록을 불러오기"""
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as log_file:
                return json.load(log_file)
        return []

    def run_cleanup_scheduler(self):
        """자동화된 파일 정리 작업을 스케줄링"""
        schedule.every(1).day.at("00:00").do(self.cleanup_files)  # 매일 자정에 파일 정리

        # 스케줄러가 백그라운드에서 실행되도록 스레드로 실행
        def run():
            while True:
                schedule.run_pending()
                time.sleep(1)

        # 스케줄러를 별도의 스레드에서 실행
        thread = threading.Thread(target=run)
        thread.daemon = True  # 메인 프로그램 종료 시 스레드도 종료되도록 설정
        thread.start()