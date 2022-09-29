import requests
import json
from sqlalchemy import create_engine, text
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.orm import registry, Session 
from datetime import datetime, timedelta
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

# SQL문
#CREATE TABLE tbl_crawling_data (
#    id INTEGER AUTO_INCREMENT PRIMARY KEY,
#    name VARCHAR(255),
#    content VARCHAR(255),
#    link VARCHAR(1024),
#    additional VARCHAR(1024),
#    startDate DATETIME
#);

registry = registry()
Base = registry.generate_base()
# class 클래스이름(상속클래스):
class TblCrawlingData(Base):
    __tablename__ = "tbl_crawling_data"

    # id는 Base 클래스에 정의되어 있다.
    id = Column(Integer, primary_key=True) # id : base 클래스에 정의 - 자동으로 번호 증가하며 부여
    name = Column(String(255)) # name : 분야 / ( 프로젝트 / 텍스트 / 마감 )
    content = Column(String(1024)) # 제목 ( title )
    additional = Column(String(1024)) # 추가 정보 - 사용하는 언어 혹은 프레임워크  리스트
    startDate = Column(DateTime(timezone=True), default=func.now()) # 시작 예정일
    link = Column(String(255))

    #def __init__(self, name, content, additional, startDate):
    #    self.name = name
    #    self.content = content
    #    self.additional = additional
    #    self.startDate = startDate

    # 객체를 문자열로 반환하는 함수
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, content={self.content!r}, additional={self.additional!r}, startDate={self.additional!r}, link={self.link!r})"

# -- 코드를 하나로 모으면 좋은 이유 ---
class Repo(object):
    def __init__(self):
        self.engine = create_engine(
            # mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
            "mysql+pymysql://username:passwd-@host:3306/dbname?charset=utf8mb4",
            echo=True,
            future=True,
        )

        #self.mapper_registry = registry()
        #self.Base = self.mapper_registry.generate_base()

        self.session = Session(self.engine)

# id , name , content , additional , startDate , link

    def add_crawling_data(self, name: str, content: str, additional: str, startDate:datetime, link: str):
        self.session.add(TblCrawlingData(name=name, content=content, additional=additional, startDate=startDate, link=link))
        self.session.commit()

    def get_crawling_data(self, name):
        query = self.session.query(TblCrawlingData)
        
        query = query.filter(TblCrawlingData.name == name, TblCrawlingData.startDate >= datetime.now()-timedelta(days=7))
        return query.all()
