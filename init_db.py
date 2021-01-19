import requests
from bs4 import BeautifulSoup
from flask import jsonify
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsubway


my_api_key = ''


# DB에 저장할 영화인들의 출처 url을 가져옵니다.
def get_station():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('http://swopenAPI.seoul.go.kr/api/subway/41787955437178773839477943464e/json/realtimeStationArrival/0/5/서울', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    subway_data = requests.get('http://swopenAPI.seoul.go.kr/api/subway/41787955437178773839477943464e/json/realtimeStationArrival/0/5/서울')


    db.dbsubway.insert_many(data)

    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})



# 출처 url로부터 영화인들의 사진, 이름, 최근작 정보를 가져오고 mystar 콜렉션에 저장합니다.
def insert_star(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('http://swopenAPI.seoul.go.kr/api/subway/41787955437178773839477943464e/json/realtimeStationArrival/0/5/서울', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    db.dbsubway.insert()
    print('완료!')


# 기존 mystar 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
    db.dbsubway.drop()  # mystar 콜렉션을 모두 지워줍니다.
    urls = get_station()
    for url in urls:
        insert_star(url)


### 실행하기
insert_all()