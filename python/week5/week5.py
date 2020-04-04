from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('indexwk5.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    memos = list(db.memos.find({}, {'_id':0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success',
                    'memos' : memos
                    # 'msg':'GET 연결되었습니다!'
                    })

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    # 2. meta tag를 스크래핑하기
    # url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0011522782'
    url_receive = request.form['url']
    comment = request.form['comment']
    # print(url_receive)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    # print(soup.select('meta'))
    og_title = (soup.select_one('meta[property="og:title"]'))
    og_url = (soup.select_one('meta[property="og:url"]'))
    og_image = (soup.select_one('meta[property="og:image"]'))
    og_description = (soup.select_one('meta[property="og:description"]'))

    title = (og_title['content'])
    url = (og_url['content'])
    image = (og_image['content'])
    description = (og_description['content'])

    db.memos.insert_one({
        'title': title,
        'url': url,
        'image': image,
        'description': description,
        'comment': comment
    })

    return jsonify({
        'result': 'success',
        'msg': '저장에 성공했습니다'
    })

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)