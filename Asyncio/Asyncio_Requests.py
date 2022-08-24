import requests
import time
import asyncio
from functools import partial
from bs4 import BeautifulSoup


async def get_text_from_url(url, keyword):
    print(f"Send {keyword} to Naver News")
    response = requests.get(url+'/'+keyword)
    print(f"Take {keyword} from Naver News")

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")

    for link in links:  # 태그 안에 텍스트요소를 가져온다
        title = link.text
        url = link.attrs['href']  # href의 속성값을 가져온다.
        print(title, url)

    print(f'-----------------END OF {keyword}---------------------------------')

async def main():
    url = "https://search.naver.com/search.naver?"+"where=news&sm=tab_jum&query="
    keywords = ['삼성전자', 'LG디스플레이', '현대건설', '롯데제과', '두산중공업',
            '네이버', '카카오', '라인', '쿠버네티스', '배달의민족',
            '당근마켓', '토스', '스타벅스', '맥도날드' ]
    
    await asyncio.gather (
        get_text_from_url(url, keywords[0]),
        get_text_from_url(url, keywords[1]),
        get_text_from_url(url, keywords[2]),
        get_text_from_url(url, keywords[3]),
        get_text_from_url(url, keywords[4]),
        get_text_from_url(url, keywords[5]),
        get_text_from_url(url, keywords[6]),
        get_text_from_url(url, keywords[7]),
        get_text_from_url(url, keywords[8]),
        get_text_from_url(url, keywords[9]),
        get_text_from_url(url, keywords[10]),
        get_text_from_url(url, keywords[11]),
        get_text_from_url(url, keywords[12]),
        get_text_from_url(url, keywords[13]),
    )

    #futures = [asyncio.ensure_future(get_text_from_url(
    #    url, keyword)) for keyword in keywords]
    #await asyncio.gather(*futures)


if __name__ == "__main__":
    start = time.time()

    # 이벤트 루프 정의
    loop = asyncio.get_event_loop()
    # 이벤트 루프 실행
    loop.run_until_complete(main())

    end = time.time()
    print(f'time taken: {end-start}')