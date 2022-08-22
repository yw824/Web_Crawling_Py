from bs4 import BeautifulSoup
import requests

# naver 서버에 대화를 시도
response = requests.get("https://www.naver.com")

# naver에서 html을 줌
html = response.text

# html 번역선생님으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')  # html 코드 , html 번역 선생님

# id 값이 NM_set_home_btn인 객체 하나를 찾아냄
word = soup.select_one("#NM_set_home_btn")  # id에서는 맨 앞에 # 필요

# 텍스트 요소만 출력
print(word.text)
