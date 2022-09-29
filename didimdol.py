from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
from urllib import request

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

# 웹사이트 열기
pages = 192
for i in range(1, pages + 1):
    #browser.get(f'https://ebook.didimdol.co.kr/TclassC/View_S/2017/1710710/assets/pages/{i}.jpg')
    #browser.implicitly_wait(1) # 로딩이 끝날 때까지 10초까지는 기다려줌
    savename = f'{i}.jpg'

    mem = request.urlopen(f'https://ebook.didimdol.co.kr/TclassC/View_S/2017/1710710/assets/pages/{i}.jpg').read()
    with open(savename, mode="wb") as f:
        f.write(mem)
        print("저장되었습니다.")

#https://ebook.didimdol.co.kr/TclassC/View_S/2017/1710710/assets/pages/9.jpg
