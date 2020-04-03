from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('taco.html')


## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    name = request.form['name_give']
    quantity = request.form['quantity_give']
    address = request.form['address_give']
    phone = request.form['phone_give']

    print(name)
    print(quantity)
    print(address)
    print(phone)

    db.orderList.insert_one({
        'name': name,
        'quantity': quantity,
        'address': address,
        'phone': phone
    })

    return jsonify({'result': 'success', 'msg': '주문, 성공적, 접수'})


# @app.route('/reviews', methods=['GET'])
# def read_reviews():
#     return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    order = list(db.orderList.find({}, {'_id': False}))
    print(order)
    return jsonify({
        'result': 'success',
        'msg': '주문 확인!',
        'data': order
    })



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)