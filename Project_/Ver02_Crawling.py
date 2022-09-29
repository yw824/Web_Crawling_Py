import requests
import json

# limit만 내가 수정해서 크롤링 하면 , 된다.
url = "https://api.holaworld.io/api/posts?sort=-createdAt&offset=0&limit=1000&isClosed=false&type=0"
response = requests.get(url)

data = json.loads(response.text)
for i in data:
    print("language : ", i.get("language"))
    print("title : ", i.get("title"))
    # print(i.get("hashTags")) # 대부분 None이라고 나옴
    print("startDate : ", i.get("startDate"))
    print("id : ", i.get("_id"))
    print("----")

print(data[0].keys())
print(data[0].values())

# language = 언어 리스트
# isClosed = boolean 값
# startDate = '2022-09-04T15:16:00.000Z'
# endDate : 없는 듯
# comments = 댓글 딕셔너리 리스트
# id = 스터디에 지정된 id primary key 값

