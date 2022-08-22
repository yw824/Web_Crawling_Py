# requests 사용법
# 먼저 vscode의 터미널에서 pip install requests 코드를 통해 requests 라이브러리를 다운받는다.

import requests


if __name__ == "__main__":
    response = requests.get("https://naver.com")
    html = response.text
    print(html)
