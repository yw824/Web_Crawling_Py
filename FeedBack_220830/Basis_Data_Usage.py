# 1. 공지사항
# 2. 스터디
data = {"name": "공지사항...", "content": "공지사항 내용...", "created_at": "2021-01-01 00:00:00"}

# 코드로 다룰 때 어떻게 다뤄야하는가
# Controller -> Service -> Repository
# Controller -> Service -> Repository -> DB
# ORM
from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://root:tiger@localhost:3306/udl?charset=utf8mb4",
    echo=True,
    future=True,
)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

from sqlalchemy import Table, Column, Integer, String

from sqlalchemy.orm import registry, Session

mapper_registry = registry()
Base = mapper_registry.generate_base()

# -- auto-generated definition
# CREATE TABLE tbl_crawling_data
# (
#   id      int AUTO_INCREMENT # 
#     PRIMARY KEY,
#   name    varchar(255)  NULL,
#   content varchar(1024) NULL,
#   additional varchar(1024) NULL # 제공하는 언어
# );


class TblCrawingData(Base):
    __tablename__ = "tbl_crawling_data"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    content = Column(String)

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, content={self.content!r})"


session = Session(engine)
# session.add(User(name="공지사항", content="내용"))
# session.commit()

query = session.query(TblCrawingData).filter(TblCrawingData.name == "공지사항")
query_data = query.all()

print(query_data[0].name)
print(query_data[0].content)

# -- 코드를 하나로 모으면 좋은 이유 ---
class Repository(object):
    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://root:tiger@localhost:3306/udl?charset=utf8mb4",
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
repo.add_crawling_data(name=data.get("name"), content=data.get("content"))
crawling_data = repo.get_crawling_data(name="공지사항")

for datum in crawling_data:
    print(datum.name)