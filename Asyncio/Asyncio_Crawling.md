# 파이썬에서 비동기 프로그래밍 활용하기

- 출처 : https://sjquant.tistory.com/15
- Github 소스 코드 : https://github.com/yw824/Web_Crawling_Py/tree/main/Asyncio

- 비동기적 방식을 이용하면 네트워크의 IO의 지연 때문에 
> 낭비되는 시간을 줄일 수 있다.

- 온라인 사전 사이트에서 단어들의 의미를 크롤링하는 코드를 작성한다고 가정하자. 

## 동기적 방식 이용하기

- 소스 코드 : Synched_Request.py

1. requests , BeautifulSoup, time 모듈을 import

2. keyword 별로 매 loop을 순회
    - 매 loop마다 request와 response를 받아와야 하기 때문에
    > 시간이 매우 많이 걸린다.
    - 실행 시간 : 2.4508297443389893

## 비동기적 방식 이용하기( Asyncio )

- 소스 코드 : Asyncio_Requests.py

- requests는 비동기적으로 작성되지 않았기 때문에
> `loop.run_in_executor`를 통해 쓰레드를 만드는 방식을 사용한다.

- 함수 앞에 `async`를 붙이면 코루틴을 만들 수 있다.
- 병목이 발생해서 다른 작업으로 통제권을 넘겨줄 필요가 있는 부분에서는 `await`을 사용한다.

- 실행 시간 : 2.4330129623413086 ( 어떤 때는 동기 방식보다 빠르기도 하고 느리기도 하다.)


## 비동기적 방식 이용하기( asyncio + aiohttp )
- requests 모듈은 코루틴으로 만들어진 모델이 아니기 때문에, 위의 Asyncio와 Requests를 사용하는 모델은 내부적으로 쓰레드를 만들어 동작한다.
- 따라서, 요청의 수가 많아질 수록 `컨텍스트 스위칭 비용`이 발생한다.

- 비동기 HTTP 통신 라이브러리인 `aiohttp`를 이용하면 코루틴을 이용한 비동기 방식을 이용할 수 있다.

- 소스 코드 : asyncio_aiohttp.py
- 실행 시간 : 1.5966527462005615 ( 대부분 동기 방식보다 1/2 정도의 시간이 나온다. )