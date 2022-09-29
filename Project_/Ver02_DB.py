import requests
import json

# limit만 내가 수정해서 크롤링 하면 , 된다.
url = "https://api.holaworld.io/api/posts?sort=-createdAt&offset=0&limit=1000&isClosed=false&type=0"
response = requests.get(url)

data = json.loads(response.text)
for i in data:
    print(i.get('isClosed')) # 마감 여부
    print(i.get("language")) # 사용 언어
    print(i.get("title")) # 타이틀
    print(i.get("hashTags")) # 해시태그 - 대부분 없다고 나옴
    print(i.get("startDate")) # 시작  날짜
    print("----")

    # print(i.keys()) # 각 항목의 key를 얻을 수 있다.

################################################# 여기까지가 크롤링 부분 #########################################

from sqlalchemy import create_engine, text

# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
engine = create_engine(
    "mysql+pymysql://root:tiger@localhost:3306/project_?charset=utf8mb4",
    echo=True,
    future=True,
)

# SQL문
# -- auto-generated definition
# CREATE TABLE tbl_crawling_data
# (
#   id      int AUTO_INCREMENT
#     PRIMARY KEY,
#   name    varchar(255)  NULL,
#   content varchar(1024) NULL
# );

############# 여기까지 OK

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry, Session  

# -- 코드를 하나로 모으면 좋은 이유 ---
class Repository(object):
    def __init__(self):
        self.engine = create_engine(
            # mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
            "mysql+pymysql://scott:tiger@localhost:3306/project_?charset=utf8mb4",
            echo=True,
            future=True,
        )

        self.mapper_registry = registry()
        self.Base = self.mapper_registry.generate_base()

        self.session = Session(self.engine)

    def add_crawling_data(self, name: str, content: str):
        self.session.add(TblCrawingData(name=name, content=content))
        self.session.commit()

    def get_crawling_data(self, name: str):
        query = self.session.query(TblCrawingData)
        query = query.filter(TblCrawingData.name == name)
        return query.all()

repo = Repository()
