from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)



app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsubway  # 'dbsubway'라는 이름의 db를 만들거나 사용합니다.




@app.route('/')
def home():
    return render_template('index.html')

##@app.route('/http://swopenAPI.seoul.go.kr/api/subway/41787955437178773839477943464e/json/realtimeStationArrival/0/5/서울', methods=['GET'])
##def test_post():
    # 1. 클라이언트로부터 데이터를 받기
   # title_receive = requests.args.get('http://swopenAPI.seoul.go.kr/api/subway/41787955437178773839477943464e/json/realtimeStationArrival/0/5/서울')
   # print(title_receive)
    # 2. meta tag를 스크래핑하기
    # 3. mongoDB에 데이터 넣기
    #return jsonify({'result': 'success', 'msg':'GET 연결'})

## API 역할을 하는 부분

## def insert_all():
##    headers = {
##        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
##    data = requests.get('http://swopenAPI.seoul.go.kr/api/subway/41787955437178773839477943464e/json/realtimeStationArrival/0/5/서울', headers=headers)


##    db.dbsuway.insert(data)
##    print(data)

##    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})

@app.route('/memo', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    bstatnNm = request.form['url_give'] #클라이언트로부터 역 이름을 받는 부분

    # 2. OPEN API 호출하기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('http://swopenAPI.seoul.go.kr/api/subway/41787955437178773839477943464e/json/realtimeStationArrival/0/5/서울',
        headers=headers)



    # 3. mongoDB에 데이터 넣기
    db.dbsubway.insert(data)

    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})

@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.dbsubway.find({}, {'_id': 0}))
    # 2. dbsubway라는 키 값으로 지하철역 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})





def db_insert():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('http://swopenAPI.seoul.go.kr/api/subway/41787955437178773839477943464e/json/realtimeStationArrival/0/5/서울',
        headers=headers)

    db.insert(data)

    return jsonify({'result': 'success', 'msg':'저장완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


