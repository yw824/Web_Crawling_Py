import requests
from bs4 import BeautifulSoup
import urllib.request
from datetime import date

url = "https://ssudorm.ssu.ac.kr:444/SShostel/mall_main.php?viewform=B0001_foodboard_list&board_no=1"
res = urllib.request.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

table = soup.find("table", attrs={"class": "boxstyle02"})
dorm_trs = table.find_all("tr")

dorm_today = date.today().weekday() + 1
for d in dorm_trs[dorm_today].find_all("td"):
    print(d.get_text().strip())
    print()


class TblCrawlingData(object):
    day: date
    eat_time: enum("breakfast", "lunch", "dinner")
    menu: str

TblCrawlingData(day=date.today(), eat_time="breakfast", menu="")
TblCrawlingData(day=date.today(), eat_time="dinner", menu="")
TblCrawlingData(day=date.today(), eat_time="lunch", menu="")

# SELECT * FROM TblCrawlingData WHERE day= '2022-08-31' AND eat_time = "breakfast"

# for index, dorm in enumerate(dorm_trs[dorm_today].find_all("td")):
#     if index == 0:
#         print("[아침]\n" + dorm.text.strip())
#         print()
#     elif index == 1:
#         print("[점심]\n" + dorm.text.strip())
#         print()
#     elif index == 2:
#         print("[저녁]\n" + dorm.text.strip())
#         print()