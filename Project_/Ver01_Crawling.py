from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 알 수 없는 오류가 발생해서 구글링으로 넣어놓은 코드
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 브라우저 생성
browser = webdriver.Chrome('chromedriver.exe')

# 웹사이트 열기
browser.get('https://holaworld.io/')
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초는 기다려줌

# 분야 메뉴 클릭( 인기 / 프론트엔드 / 백엔드 / 모바일 / 기타 / 모두보기 )
range = browser.find_element(By.XPATH, '//li[text()="백엔드"]')
time.sleep(2)
print(range.text) # 백엔드 탭 선택
range.click()

# 백엔드 - 파이썬 언어 필터 사용한다고 가정하고 크롤링
language = browser.find_element(By.XPATH, '//span[text()="Python"]')
time.sleep(2)
language.click()

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
bundle = browser.find_element(By.CSS_SELECTOR, '.studyList_studyList__3xoys')
# a 리스트의 클래스명 : studyItem_studyItem__1Iipn studyItem_open__1PGn-
# 아마도 중간에 띄어쓰기가 인식이 안 되는 것 같다.


items = bundle.find_elements(By.TAG_NAME, 'a')
# 각 요소 : <selenium.webdriver.remote.webelement.WebElement (session="81b8e364b390a9383bb4f6e8df817cc2", 
#           element="42552a2b-b556-4d31-b2e4-6991924e1169")>

for item in items:
    print('--------------------------------------------------')
    title = item.find_element(By.CSS_SELECTOR, '.studyItem_title__2B_2o').text
    # date = item.find_elements(By.TAG_NAME, 'p') # 세션으로 나온다.
    link = item.get_attribute('href')
    print("title : ", title)
    #  print("date : ", date)
    print("link : ", link)
    

###################### 220830 피드백 후 더이상 사용하지 않습니다 #########################
