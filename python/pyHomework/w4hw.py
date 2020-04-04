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
@app.route('/order', methods=['POST'])
def post_order():
    name_post = request.form['name_give']
    quantity_post = request.form['quantity_give']
    address_post = request.form['address_give']
    phone_post = request.form['phone_give']

    db.orders.insert_one({
        'name': name_post,
        'quantity': quantity_post,
        'address': address_post,
        'phone': phone_post
    })

    return jsonify({
        'result': 'success',
        'msg': 'post 주문 접수 성공~!'})




@app.route('/order', methods=['GET'])
def submitOrder():
    orders = list(db.orders.find({}, {'_id': 0}))
    # print(orders)
    return jsonify({
        'result': 'success',
        'msg': '주문 완료!',
        'orders': orders
        })



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)