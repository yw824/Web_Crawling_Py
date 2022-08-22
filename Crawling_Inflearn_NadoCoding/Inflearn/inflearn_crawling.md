## 인프런 - 크롤링 도입

#### 크롤링이 중요한 이유
- 돈을 버는 것보다 시간을 버는 것이 중요하다.
- 크롤링을 통해 시간을 벌 수 있다.

#### 크롤링 강의 - 학습 내용
- 크롤링 핵심 기초를 2시간 만에 학습
- 크롤링 라이브러리 사용법( beautifulsoup, selenium, openpyxl )
- 네이버 뉴스, 주식 현재가, 네이버쇼핑 데이터 수집 프로그램

#### 학습 효과
- 크롤링이 어떤 것인지 쉽고 빠르게 알게 된다.
- 크롤링 맛보기
- ( 기본편이라 ) 내가 원하는 웹사이트의 크롤링은 어려울 수 있음


#### 주의사항
- 크롤링한 데이터를 무분별하게 상업적으로 이용하지 않는다.
    - 원작자의 동의 없이 데이터를 수집하고 상업적으로 이용하거나 타 웹사이트에 업로드하는 행위는 처벌 대상이 될 수 있다.
- 대상 서버에 부담을 주지 않도록 한다.
    - 네이버 , 구글 등 대형 서버는 크롤링으로 인한 트래픽 초과 등 영향이 적지만 
    - 작은 웹사이트의 서버는 크롤링으로 인해 트래픽 과다가 발생하여 서버가 멈출 수도 있다. 
        - 이는 영업 방해의 행위가 되고, 처벌 대상이다. 


## requests 라이브러리

#### HTTP통신 - Get 방식
- 특정 사이트를 보여달라는 요청 
- 서버에서 특정 사이트의 html 파일을 불러와서 사용자에게 보여주는 방식

#### HTTP통신 - Post 방식
- 사용자가 직접 정보를 입력하여 , 이 정보들과 함께 특정 사이트의 결과를 요청하는 것
- 서버는 해당 정보들을 가지고 특정 연산을 수행하여 그 연산의 결과를 사이트에 담아 출력한다.

#### 내부 / 외부 라이브러리
- 내부 라이브러리 : 특정 언어에서 기본적인 작동을 위해 제공하는 라이브러리 - 프로그래밍 언어의 설치와 동시에 이루어진다.
- 외부 라이브러리 : 기본 라이브러리가 아니라서 추가적으로 설치가 필요한 라이브러리

requests 라이브러리 사용법 : CH03_requests.py <br>

## beautifulsoup 설치

- 코드 형식  = Beautifulsoup(html 코드, html 번역 선생님) <br>
beautifulsoup 라이브러리 사용법 : CH03_beautifulsoup.py <br>

## CSS 선택자

- CSS : 웹사이트의 디자인을 표현하기 위한 언어
- CSS 선택자 : 디자인을 변경할 HTML 태그를 선택하는 것
    = 크롤링할 HTML 태그를 선택하는 것

1. 태그 선택자 : 태그의 이름으로 선택한다.
    - h1, a 등
2. id 선택자 : 태그의 id 값로 선택한다.
    - #id명
3. class 선택자 : 태그 그룹명(class명)으로 선택한다.
    - .class명
4. 자식 선택자 : 보통 내가 원하는 태그에 별명이 없을 때 사용
    - 바로 아래에 있는 태그를 선택
    - .클래스명 > 태그 선택자 의 형식

## URL

- 인터넷 주소 형식
- 4가지 구성 요소로 구성된다.
    1. Protocol : 프로토콜
    2. Domain : IP 주소에 이름을 준 것
    3. Path : 서버에서 해당 페이지까지의 경로
    4. Parameter : 서버에게사용자가 부여한 데이터

- https://search.naver.com/search.naver?where=news&query=삼성전자라는 URL이 있다고 하자.

1. Protocol : https( :// 이전까지 )
2. Domain : search.naver.com( :// 이후부터 / 전까지 )
3. Path : search.naver( / 다음부터 ? 전까지 )
4. Parameter : where=news&query=삼성전자( ? 이후부분 )
    - 각 인자들의 구분은 &으로 구분
    - 각 인자들은 key=value 형식으로 구분됨
    - 검색어에 해당



## 실전 프로젝트 1 : 뉴스 데이터 수집하기

#### 뉴스의 제목과 링크를 가지고 오자

삼성전자를 네이버 검색어에 입력한 후 뉴스 제목과 html 주소를 크롤링할 예정이다. <br>

- 먼저 내가 원하는 정보가 어떤 html로 구성되어 있는지 확인한다.

- F12 버튼을 눌러 개발자 도구에 들어간 후 , 태그에 보면 , 뉴스 태그의 별명이 .news_tit인 것으로 확인 가능
- Ctrl + F 키를 누른 후 , .news_tit 을 누르면 전체 제목 바가 검색된다.
> 이를 이용하여 파일을 생성한 후, 뉴스 제목 태그를 가져올 것이다.
- 코드 : 05.뉴스제목과링크가져오가.py

#### 검색어에 따라 다른 결과를 나타내기 : pyautogui

- 마우스, 키보드 매크로 라이브러리
- 간단한 입력 창 띄우기
예시 : pyautogui.prompt("검색어를 입력하세요") <br>

#### 반복문으로 여러 페이지 결과 가져오기
> 이동하면서 URL이 어떻게 변하는 지 살펴보자
> 웹 사이트에서 확인하기

> 1페이지 : https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=53&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1

> 3페이지 : https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=84&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=21

- 다른 것은 바뀌지 않고 , query 중  
> cluster_rank 및 start의 key값을 가진 value값만 바뀐다.
- 이 중 start가 10단위로 증가하는 것 같다. ( cluster_rank는 중요하지 않은 것 같다. )

> 1페이지 : 1 / 2페이지 : 11 , 3페이지 : 21 ,,,
> 10번 반복문을 실행하면 될 것 같다.

- 실행 코드 : 07.여러페이지가져오기.py


## 실전 프로젝트 2 : 네이버 주식 현재가 크롤링

네이버 국내증시 주식 사이트의 현재가를 종목별로 엑셀에 정리하고 싶다. <br>

#### 준비물 : 
- 파이썬 변수 , 리스트 , 반복문
- 크롤링 쌩기초( requests, BeautifulSoup )

#### 사이트 분석
- 네이버 증권창에 삼성전자 키워드를 검색한 다음 , 결과 창에서 F12를 눌러 개발자 창으로 이동한다. 
- td 표에서 현재가 항목 id : #_nowVal , class : .tah p11
- URL : https://finance.naver.com/item/sise.naver?code=005930
    - 005930 : 삼성전자의 종목 코드

- 코드 : 08_네이버_주식_크롤링/01.데이터추출.py

#### 파이썬으로 엑셀 다루는 방법 - 수집한 데이터 엑셀에 저장하기

1. 라이브러리 설치 : openpyxl
    - 파이썬에서 엑셀을 쉽게 다룰 수 있도록 도와주는 라이브러리
    - pip install openpyxl

2. 코드 : 08_네이버_주식_크롤링/
    - 02_엑셀만들기.py
    - 03_엑셀불러오기.py


3. 공식 문서
    - 프로그램을 개발한 사람들이 사용자에게 사용법을 알려주는 사이트
    




