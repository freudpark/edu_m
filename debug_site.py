
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.goedy.kr/goedy/main.do"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive'
}

print(f"Checking {url}...")

try:
    session = requests.Session()
    response = session.get(url, headers=headers, verify=False, timeout=10)
    print(f"Status: {response.status_code}")
    response.raise_for_status()
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
