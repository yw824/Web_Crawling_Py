import requests
from bs4 import BeautifulSoup
import time

# 3.beautifulsoup.py 를 차용
url = "https://search.naver.com/search.naver?"+"where=news&sm=tab_jum&query="
keywords = ['삼성전자', 'LG디스플레이', '현대건설', '롯데제과', '두산중공업',
            '네이버', '카카오', '라인', '쿠버네티스', '배달의민족',
            '당근마켓', '토스', '스타벅스', '맥도날드' ]

start = time.time()
for keyword in keywords:
    print(f"Send {keyword} to Naver News")
    response = requests.get(
        "https://search.naver.com/search.naver?"+"where=news&sm=tab_jum&query="+keyword)
    print(f"Take {keyword} from Naver News")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select(".news_tit")

    for link in links:  # 태그 안에 텍스트요소를 가져온다
        title = link.text
        url = link.attrs['href']  # href의 속성값을 가져온다.
        print(title, url)
    print(f'-----------------END OF {keyword}---------------------------------')

end = time.time()
print(f'time taken: {end-start}')