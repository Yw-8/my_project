import requests
from bs4 import BeautifulSoup
from flask import jsonify
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsubway5


my_api_key = ''


def db_insert():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('http://swopenAPI.seoul.go.kr/api/subway/41787955437178773839477943464e/json/realtimeStationArrival/0/5/서울',
        headers=headers)


    subdata = data.json()
    print(data.json())
    db.dbsubway5.insert_one(subdata)



db_insert()