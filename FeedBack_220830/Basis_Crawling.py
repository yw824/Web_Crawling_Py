import requests
import json
from bs4 import BeautifulSoup

# limit만 내가 수정해서 크롤링 하면 , 된다.
url = "https://api.holaworld.io/api/posts?sort=-createdAt&offset=0&limit=1000&isClosed=false&type=0"
response = requests.get(url)
print(response)


# json 문자열에는 link가 없다.
data = json.loads(response.text) # json 문자열을 python 객체로 변환
print(data[0].keys())
for i in data:
    print(i.get('id'))
    print("----")