
import requests
import subprocess
import platform
import urllib3

# Suppress InsecureRequestWarning specifically for this use case
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class WebsiteMonitor:
    def __init__(self):
        self.urls = {}

    def load_urls(self, file_path):
        """Loads URLs from the specified text file."""
        self.urls = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='cp949') as f:
                lines = f.readlines()
        except FileNotFoundError:
            pass
        
        for line in lines:
            parts = line.split()
            if len(parts) >= 2:
                name = parts[0]
                url = parts[1]
                self.urls[name] = url

    def get_urls(self):
        """Returns the dictionary of URLs."""
        return self.urls

    def check_site(self, url):
        """Checks a single URL with a retry mechanism. Disables SSL verification."""
        # Enhanced headers to mimic a real browser to avoid 400 Bad Request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
        }
        
        def translate_error(error_msg):
            msg = str(error_msg).lower()
            if "name or service not known" in msg or "getaddrinfo failed" in msg:
                return "사이트 주소(도메인)를 찾을 수 없습니다."
            if "connect" in msg and "refused" in msg:
                return "사이트 연결이 거부되었습니다. (서버 다운 추정)"
            if "timed out" in msg or "timeout" in msg:
                return "응답 시간이 초과되었습니다. (접속 지연)"
            if "ssl" in msg or "certificate" in msg:
                return "보안 인증서 오류가 발생했습니다."
            if "404" in msg:
                return "페이지를 찾을 수 없습니다. (404 Not Found)"
            if "400" in msg:
                return "잘못된 요청입니다. (400 Bad Request - 브라우저 헤더 필요)"
            if "500" in msg:
                return "서버 내부 오류입니다. (500 Internal Server Error)"
            if "502" in msg or "503" in msg:
                return "서버가 일시적으로 사용 불가능합니다. (502/503)"
            return f"접속 실패: {error_msg}"

        try:
            session = requests.Session()
            # verify=False handles sites with self-signed or local government certs
            response = session.get(url, timeout=15, verify=False, headers=headers)
            response.raise_for_status()
            return True, None
        except requests.RequestException:
            # Retry once
            try:
                session = requests.Session()
                response = session.get(url, timeout=15, verify=False, headers=headers)
                response.raise_for_status()
                return True, None
            except requests.RequestException as e:
                return False, translate_error(str(e))

    def check_network(self):
        """Checks intenet connectivity by connecting to Google DNS."""
        import socket
        try:
            # Connect to Google DNS on port 53 (DNS)
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False

    def log_error(self, message):
        """Appends an error message to the log file with a timestamp."""
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        try:
            with open("check_error.log", "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception:
            pass

    def run_check(self):
        """Checks all loaded URLs in parallel and returns failed sites."""
        import concurrent.futures
        
        failed_sites = []
        is_network_up = self.check_network()

        if not is_network_up:
            self.log_error("Network Error: Cannot connect to internet (Google DNS check failed).")
            return {'network_error': True, 'failed_sites': []}

        # Helper function for threading
        def check_single_url(item):
            name, url = item
            success, error = self.check_site(url)
            return name, url, success, error

        # Run checks in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_url = {executor.submit(check_single_url, item): item for item in self.urls.items()}
            
            for future in concurrent.futures.as_completed(future_to_url):
                name, url, success, error = future.result()
                if not success:
                    self.log_error(f"Site Fail: {name} ({url}) - {error}")
                    failed_sites.append({'name': name, 'url': url, 'error': error})

        return {'network_error': False, 'failed_sites': failed_sites}

if __name__ == "__main__":
    # Test run
    monitor = WebsiteMonitor()
    monitor.load_urls("지역교육청_url.txt")
    result = monitor.run_check()
    print(result)
