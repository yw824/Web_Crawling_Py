import requests
from bs4 import BeautifulSoup
import pyautogui


keyword = pyautogui.prompt("검색어를 입력하세요 >>> ")
pageNum = 1
lastPage = pyautogui.prompt("마지막 페이지 번호를 입력해 주세요 >>> ")
# 한글 URL은 query 뒤의 특정 문자들로 인코딩 된다.
for i in range(1, int(lastPage) * 10, 10):
    print(f"{pageNum} 입니다===================================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select(".news_tit")
    # print(links)  # 실행 결과 : 리스트 형태로 나온다.

    for link in links:  # 태그 안에 텍스트요소를 가져온다
        title = link.text
        url = link.attrs['href']  # href의 속성값을 가져온다.
        print(title, url)
    pageNum += 1
