import requests
import json
from temp_DB import Repo
from temp_DB import TblCrawlingData
from datetime import datetime
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # limit만 내가 수정해서 크롤링 하면 된다.
    url = "https://fun.ssu.ac.kr/ko/program/all/list/all/1"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    elements  = soup.select(".date_title")
    for element in elements:
        if element.text == '운영:':
            continue
        print(element.text)
