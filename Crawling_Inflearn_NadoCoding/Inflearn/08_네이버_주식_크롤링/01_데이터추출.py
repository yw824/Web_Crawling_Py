import requests
from bs4 import BeautifulSoup

# 종목 코드 리스트
codes = [
    '005930',  # 삼성전자
    '006660',  # SK하이닉스
    '035720'  # 카카오
]

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal")
    print(price)  # 현재가 정보
    print(price.text.replace(',', ''))  # 현재가 중 실제 값만 해당
