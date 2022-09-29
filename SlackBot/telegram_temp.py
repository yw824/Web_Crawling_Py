import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import telegram
import time


bot = telegram.Bot(token="텔레그램토큰")


def movie_alarm_telegram(areacode='01', theatercode='0013', date='20211215', check_title='스파이더맨-노 웨이 홈', chat_ids=['chat_id', 'chat_id']):
    movie_dict = {}
    
    url = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode={areacode}&theatercode={theatercode}&date={date}"

    url_req = requests.get(url)
    url_soup = BeautifulSoup(url_req.text, 'html.parser')

    movie_titles = []
    
    movie_infos = url_soup.select("div.col-times > div.info-movie")
    if (movie_infos):
        for movie_info in movie_infos:
            screentype_list = []
            title = movie_info.select('a > strong')[0].text.strip()

            screentypes = movie_info.parent.select("span.screentype")

            for screentype in screentypes:
                screentype_list.append(str(screentype.text))

            movie_dict[title] = ", ".join(screentype_list)

        for movie in movie_dict.keys():
            movie_open_check_condition1 = (check_title == movie)
            if True in {movie_open_check_condition1}:
                for chat_id in chat_ids:
                    bot.sendMessage(chat_id=chat_id, text = f"{movie}의 {movie_dict[movie]}예매가 오픈되었습니다.")
    else:
        bot.sendMessage(chat_id="689318726",text = "아직 오픈된 예매가 없습니다.")
        print(datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S"))
        print("fail")


if __name__ == "__main__":
    movie_alarm_telegram(areacode='01', theatercode='0013', date='20211215', check_title='스파이더맨-노 웨이 홈', chat_ids=['chat_id', 'chat_id'])

sc = BlockingScheduler()
sc.add_job(movie_alarm_telegram, 'interval', seconds = 30)
sc.start()
# 출처: https://somjang.tistory.com/entry/Python-파이썬과-텔레그램으로-스파이더맨-노웨이홈-예매-알리미-만드는-방법 [솜씨좋은장씨:티스토리]