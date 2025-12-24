
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
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        try:
            # verify=False handles sites with self-signed or local government certs
            response = requests.get(url, timeout=10, verify=False, headers=headers)
            response.raise_for_status()
            return True, None
        except requests.RequestException:
            # Retry once
            try:
                response = requests.get(url, timeout=10, verify=False, headers=headers)
                response.raise_for_status()
                return True, None
            except requests.RequestException as e:
                return False, str(e)

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
