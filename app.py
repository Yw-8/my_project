from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)



app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsubway5  # 'dbsubway5'라는 이름의 db를 만들거나 사용합니다.




@app.route('/')
def home():
    return render_template('index.html')



@app.route('/api/list', methods=['GET'])
def show_stars():
    # 1. db에서 subway 목록 전체를 검색
    stars = list(db.dbsubway5.find({}))

    return jsonify({'result': 'success', 'realTimeArrivalList': stars})

@app.route('/api/delete', methods=['POST'])
def delete_star():
    # 1. 클라이언트가 전달한 station 변수에 넣는다.
    name_station = request.form['name_give']
    db.dbsubway.delete_one({'bstatnNm': name_station})
        # 2. dbsubway라는 키 값으로 지하철역 정보 보내주기
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


