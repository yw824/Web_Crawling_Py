from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 강의와 코드가 조금 다르다. Selenium 업데이트로 인해 2022년 6월 이후 자료만 찾아보자.
# https://bskyvision.com/entry/python-selenium-%ED%81%AC%EB%A1%A4%EB%A7%81-findelementbycssselector-%EB%8D%94-%EC%9D%B4%EC%83%81-%EC%82%AC%EC%9A%A9-%EB%B6%88%EA%B0%80

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

# 웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지는 기다려줌

# 쇼핑 메뉴 클릭
# 코드가 바뀌었다. find_element_by_css_selector() 함수 더 이상 사용하지 않는다.
browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click() 
time.sleep(2)
# 네이버 웹사이트의 로딩 속도가 느리면 쇼핑 메뉴 attribute를 찾지 못할 수도 있다.
# 따라서 위의 로딩 10초 기다리는 코드가 필요

# 검색창 클릭( focus 입력하기 )
search = browser.find_element(By.CSS_SELECTOR, '._searchInput_search_input_QXUFf')
search.click()

# 검색어 입력
search.send_keys('아이폰13')
search.send_keys(Keys.ENTER)  # 엔터 키 전송

# --------------- 아이폰13 검색창에 도달한 이후 ----------------------------------

# 웹브라우저에서 자바스크립트 처리 가능한 함수 : execute_script

# 스크롤 전 높이
before_h = browser.execute_script('return window.scrollY')

# 무한 스크롤 : 무한 반복문을 사용( while true )
while True:
    # 맨 아래로 스크롤을 내린다. 키보드의 END 키를 사용
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간이 필요하기 때문에 로딩 시간 추가
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script('return window.scrollY')
    if after_h == before_h : 
        break

    before_h = after_h

# 각 상품 div 담고 있는 리스트를 가져 온다.
items = browser.find_elements(By.CSS_SELECTOR, '.basicList_info_area__TWvzp')

# 요소 개수와 타이틀 , 링크 , 가격 모두 같은 개수여야 한다. ( 사이트에서는 40개 )
for item in items:
    # 이름 : 텍스트만 추출
    name = item.find_element(By.CSS_SELECTOR, '.basicList_title__VfX3c').text
    # 가격 : 텍스트만 추출 , 판매중단이 있을 수 있으므로 예외처리
    try:
        price = item.find_element(By.CSS_SELECTOR, '.basicList_price_area__K7DDT').text
    except: # 판매 중단 : 값이 없을 때 except문 실행
        price = '판매중단'
    # 링크 : 속성으로 추출 , 자식 태그를 사용한다.
    link = item.find_element(By.CSS_SELECTOR, '.basicList_title__VfX3c > a').get_attribute('href')

    print(name, price, link)


