import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    url = "https://www.google.com"
    
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a')
    
    result_list = []
    
    for link in links:
        title = link.text
        result_list.append(title)
    
    return {
        'statusCode': 200,
        'body': json.dumps(result_list)
    }