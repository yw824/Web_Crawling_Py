import json
import requests
from temp_DB import Repo
from temp_DB import TblCrawlingData
from bs4 import BeautifulSoup
from datetime import datetime

# okky : 보통 2페이지까지가 7일 내 데이터에 해당
# url2 = 'https://okky.kr/events/gathering?page=1'

if __name__ == '__main__':

    repo = Repo()

    for i in range(1, 4):
        # 1 to 3 - 보통 3페이지까지가 모집 중 데이터에 해당
        url = f'https://fun.ssu.ac.kr/ko/program/all/list/all/{i}'

        
        # 얘는 json 타입이 아니여서 그냥 BeautifulSoup으로 크롤링해야 함
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, "html.parser")

        # SQL문
        #CREATE TABLE tbl_crawling_data (
        #    id INTEGER AUTO_INCREMENT PRIMARY KEY,
        #    name VARCHAR(255),
        #    content VARCHAR(255),
        #    link VARCHAR(1024),
        #    additional VARCHAR(1024),
        #    startDate DATETIME
        #);

    # ------------------------------------------- OPEN ------------------------------------------------------------------
        list = soup.select(".OPEN")
        #print("----------------------------OPEN------------------------------")
        for item in list:
            parent = item.parent # 부모 태그  
            # print(type(parent))

            # 제목
            content = parent.find("div", {"class": "detail"}).find("div", {"data-role": "default"}).find("div", {"class": "content"})
            title = content.find("b", {"class": "title"})
            title = title.text
            #print("제목 : ", title.text)

            # 링크
            link = 'https://fun.ssu.ac.kr'+parent['href'] 
            #print("링크 : ", link)

            # 구분
            name = 'open'
            #print("구분 : ", name)

            # 마감 일자 = duedate
            startDate = parent.find("div", {"class": 'content'}).find_all("small")[2].find_all("time")[1]
            startDate = startDate['datetime'][:10]
            startDate = datetime.strptime(startDate, '%Y-%m-%d')
            #print("마감 일자 : ", startDate['datetime'])

            # 주최
            additional = content.find('label').text # 주최 
            #print("주최 : ", additional)

            #print("----------------------------------------------------------")

            repo.add_crawling_data(name, title, additional, startDate, link)
        
    # ------------------------------------------- APPROACHING ------------------------------------------------------------------
        list = soup.select(".APPROACHING")
        # print("--------------------------APPROACHING--------------------------------")
        for item in list:
            parent = item.parent # 부모 태그  
            # print(type(parent))

            # 제목
            content = parent.find("div", {"class": "detail"}).find("div", {"data-role": "default"}).find("div", {"class": "content"})
            title = content.find("b", {"class": "title"})
            title = title.text
            # print("제목 : ", title.text)

            # 링크
            link = 'https://fun.ssu.ac.kr'+parent['href'] 
            # print("링크 : ", link)

            # 구분
            name = 'approaching'
            # print("구분 : ", name)

            # 마감 일자
            startDate = parent.find("div", {"class": 'content'}).find_all("small")[2].find_all("time")[1]
            startDate = startDate['datetime'][:10]
            startDate = datetime.strptime(startDate, '%Y-%m-%d')

            # print("마감 일자 : ", startDate['datetime']) 

            # 주최
            additional = content.find('label').text # 주최 
            # print("주최 : ", additional)

            # print("----------------------------------------------------------")

            repo.add_crawling_data(name, title, additional, startDate, link)
        
    # ------------------------------------------- APPROACH_CLOSING ------------------------------------------------------------------
        list = soup.select(".APPROACH_CLOSING")
        # print("---------------------------APPROACH_CLOSING-------------------------------")
        for item in list:
            parent = item.parent # 부모 태그  
            # print(type(parent))

            # 제목
            content = parent.find("div", {"class": "detail"}).find("div", {"data-role": "default"}).find("div", {"class": "content"})
            title = content.find("b", {"class": "title"})
            title = title.text
            # print("제목 : ", title.text)

            # 링크
            link = 'https://fun.ssu.ac.kr'+parent['href'] 
            # print("링크 : ", link)

            # 구분
            name = 'approach_closing'
            # print("구분 : ", name)

            # 마감 일자
            startDate = parent.find("div", {"class": 'content'}).find_all("small")[2].find_all("time")[1]
            startDate = startDate['datetime'][:10]
            startDate = datetime.strptime(startDate, '%Y-%m-%d')
            # print("마감 일자 : ", startDate['datetime'])

            # 주최
            additional = content.find('label').text # 주최 
            # print("주최 : ", additional)

            # print("----------------------------------------------------------")

            repo.add_crawling_data(name, title, additional, startDate, link)

        
        
