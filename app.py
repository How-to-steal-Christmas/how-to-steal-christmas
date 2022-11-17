from flask import Flask, render_template, jsonify, request, session, redirect, url_for


app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient("mongodb+srv://jominuk:alsdnr1549-@cluster0.pto4r2x.mongodb.net/?retryWrites=true&w=majority")
db = client.sparta


@app.route('/')
def home():
   return render_template('createcards.html')


@app.route("/modal", methods=["POST"])
def modal_post():
   url_receive = request.form['url_give']
   coupon_receive = request.form['coupon_give']
   comment_receive = request.form['comment_give']

   doc = {
      'url':url_receive,
      'coupon':coupon_receive,
      'comment':comment_receive
   }
   db.modal.insert_one(doc)
   return jsonify({'msg':'선물 등록!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)



# 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)
#
# # 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})
#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# all_users = list(db.users.find({},{'_id':False}))
#
# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})