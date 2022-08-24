import requests
import time
import asyncio
# aiohttp 설치 필요
import aiohttp
from bs4 import BeautifulSoup

async def get_text_from_url(url, keyword):
    print(f"Send {keyword} to Naver News")
    
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url+keyword) as res:
            text = await res.text()
    
    print(f'Take {keyword} from Naver News')
    soup = BeautifulSoup(text, 'html.parser')
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

    futures = [asyncio.ensure_future(get_text_from_url(
        url, keyword)) for keyword in keywords]
    
    await asyncio.gather(*futures)


if __name__ == "__main__":
    start = time.time()

    # 이벤트 루프 정의
    loop = asyncio.get_event_loop()
    # 이벤트 루프 실행
    loop.run_until_complete(main())

    end = time.time()
    print(f'time taken: {end-start}')