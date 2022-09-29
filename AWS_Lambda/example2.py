import json # 기본 라이브러리
import urllib.request # 기본 라이브러리 -> 곧바로 이용할 수 있다.
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    url = "https://www.google.com"
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    
    a_tags = soup.find_all("a")
    result_list = []
    for i in a_tags:
        result_list.append(i.get_text())
    
    return {
        'statusCode': 200,
        'body': json.dumps(result_list)
    }