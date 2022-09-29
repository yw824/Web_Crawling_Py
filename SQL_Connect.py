import pymysql
import requests
from bs4 import BeautifulSoup

# 예제 출처 : https://unpasoadelante.tistory.com/130

ranking = 0

############################################## MySQL DB 스키마 생성 #######################################################

# 스키마 생성 : https://goddaehee.tistory.com/278
# database 연결 , 사전에 mysql workbench에서 bestproducts 스키마 설계가 필요하다.
def sql_connect():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='tiger', db='bestproducts', charset='utf8')
    cursor = db.cursor()

    # 스키마 안에 items 테이블을 만드는 코드
    sql = '''
    CREATE TABLE items (
        item_code VARCHAR(20) NOT NULL PRIMARY KEY,
        title VARCHAR(200) NOT NULL,
        ori_price INT NOT NULL,
        dis_price INT NOT NULL,
        discount_percent INT NOT NULL,
        provider VARCHAR(100)
    );
    '''
    cursor.execute(sql)

    # 스키마 안에 ranking 테이블을 만드는 코드
    sql = '''
    CREATE TABLE ranking (
        num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        main_category VARCHAR(50) NOT NULL,
        sub_category VARCHAR(50) NOT NULL,
        item_ranking TINYINT UNSIGNED NOT NULL,
        item_code VARCHAR(10) NOT NULL,
        FOREIGN KEY(item_code) REFERENCES items(item_code)
    );
    '''

    # SQL문 실행
    cursor.execute(sql)

    # SQL 서버에 commit ( 결과물 저장 )
    # 실행한 후 MySQL WorkBench에 가서 bestproducts 스키마를 Refresh 하는 과정이 필요하다.
    db.commit()
    db.close()
    return


#################################### 크롤링 #################################################

def get_items():
# G마켓 베스트 main category 데이터 추출 
    response = requests.get('https://corners.gmarket.co.kr/Bestsellers')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    categories = soup.select(".by-cate div ul li a")

    for category in categories:
        # print(category.text)
        # print(category['href'])
        get_item(category.text, category['href']) # 각 카테고리명 및 주소 얻어 오기

    return categories


def get_item(category_name, category_link): # 각 카테고리의 item 얻어 오기

    response = requests.get('https://corners.gmarket.co.kr' + category_link) # 내려갈 필요 없음 , 베스트 딜은 1 ~ 100까지 항목 고정되어 있음
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.best-list ul li')
    
    for item in items:

        data_dict = dict()
        tag = item.select_one('.itemname')     
        o_price = item.select_one('.o-price')
        s_price = item.select_one('.s-price')
        name = tag.text
        product_link = tag['href']
        code = product_link.split('=')[1].split('&')[0]

        sales_response = requests.get(product_link)
        sales_html = sales_response.text
        sales_soup = BeautifulSoup(sales_html, 'html.parser')
        provider = sales_soup.select_one('div.item-topinfo_headline > p > span > a').text

        o_price = o_price.select_one('span:last-child') # original price
        s_price = s_price.select_one('span:last-child') # saled price

        #print("Name : ", name) # 타이틀
        #print('Code : ', code) # 상품 코드
        #print('Link : ', product_link) # 링크
        #print('Provider : ', provider) # 

        if o_price == None: # 원 상품가 - o_price가 없으면 : 세일 없는거 , s_price에 원가인 o_price 그대로 넣은 거
            o_price = s_price
        o_price = o_price.text.replace(',', '').replace('원', '')
        
        # 세일 상품가
        s_price = s_price.text.replace(',', '').replace('원', '')
        
        o_price = int(o_price)
        s_price = int(s_price)
        # 세일 비율
        rate = int(abs(s_price - o_price) / o_price * 100)

        # print('original : ', o_price)
        # print('saled : ', s_price)
        # print('sale Rate : ', rate)

        # titles = [] # 타이틀
        # codes = [] # 상품 코드
        # originals = [] # 원 상품가
        # sales = [] # 세일 상품가
        # sale_rates = [] # 세일 비율
        # providers = [] # 판매자 

        data_dict['category_name'] = category_name
        data_dict['title'] = name
        data_dict

        # print('-----------------------------')

        

        
        
        

    # print("--------------------------------------------------------------------------")


    return True


######################################### 크롤링 결과 DB에 저장 ##################################      

def save_data(data, keys):
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='tiger', db='bestproducts', charset='utf8')
    cursor = db.cursor()

    # data info 출력
    for keys in keys:
        print(key, data[key])
    
    sql = """
        SELECT COUNT(*) FROM items WHERE item_code = 
    
    """

    cursor.execute(sql)

    sql = """

    """





######################################### main 함수 ############################################

status = int(input("현재 스키마 설계 상태를 입력하세요( 구축됨 : 1 , 구축 안됨 : 0 >> "))
if status == 0:
    sql_connect()

get_items()

    # titles = [] # 타이틀
    # codes = [] # 상품 코드
    # originals = [] # 원 상품가
    # sales = [] # 세일 상품가
    # sale_rates = [] # 세일 비율
    # providers = [] # 판매자
