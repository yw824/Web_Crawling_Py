import requests
import json

# limit만 내가 수정해서 크롤링 하면 , 된다.
url = "https://api.holaworld.io/api/posts?sort=-createdAt&offset=0&limit=1000&isClosed=false&type=0"
response = requests.get(url)

data = json.loads(response.text)
for i in data:
    print(i.get("language"))
    print(i.get("title"))
    # print(i.get("hashTags"))
    print(i.get('type'), type(i.get('type')))
    print()
    print("----")

# dict_keys(['language', 'isClosed', 'views', 'likes', 'totalLikes', 'startDate', 
#            'endDate', 'type', 'recruits', 'onlineOrOffline', 'contactType', 'expectedPeriod', 
#            '_id', 'title', 'author', 'comments', 'hashTag', 'totalComments', 'id'])
