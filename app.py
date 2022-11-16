from flask import Flask, render_template, jsonify, request, session, redirect, url_for
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient("mongodb+srv://jominuk:alsdnr1549-@cluster0.pto4r2x.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.sparta

@app.route('/')
def home():
   return render_template('treeforguest.html')

#캘린더 조회하기에서 선택한 캘린더를 공유하면 받는사람이 볼수 있는 url 생성
# @app.route('/calendarget', methods=['GET'])
# def calendar_data_get():


#받는사람은 완성된 트리로 랜딩-> 일자별 열기 누르면 모달창으로 선물을 조회함
@app.route('/tree/details', methods=['GET'])
def modal_data_get():
   modals = db.modal.find_one({'calendar_name':'test'}, {'_id':False})
   print(modals)
   return jsonify({'modals': modals})



#캘린더 조회하기에서 선택한 캘린더를 삭제
# @app.route('/calendardelete', methods=['POST'])
# def calendar_delete():
#
#    db.calendar.delete_one({'name': 'bobby'})
#    cal_delete = db.calendar.find_one({'name': 'bobby'})
#    print(cal_delete)
#    return jsonify({'msg': '삭제 완료'})




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