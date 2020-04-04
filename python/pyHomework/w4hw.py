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
@app.route('/orders', methods=['POST'])
def submit_order():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    print(name_receive)
    print(quantity_receive)
    print(address_receive)
    print(phone_receive)

    orders = {
        'name': name,
        'quantity': quantity,
        'address': address,
        'phone': phone
    }

    db.orders.insert_one(order)

    return jsonify({'result': 'success', 'msg': '주문, 성공적, 접수'})




@app.route('/orders', methods=['GET'])
def submit():
  # return jsonify({'result': 'success', 'msg': '주문 완료!'})

    orders = list(db.orders.find({}, {'_id': 0}))
    print(orders)
    return jsonify({
        'result': 'success',
        'msg': '주문 완료!',
        'data': orders
    })



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)