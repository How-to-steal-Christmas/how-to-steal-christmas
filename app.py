import certifi
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import jwt
import datetime
import hashlib
app = Flask(__name__)

from pymongo import MongoClient
ca = certifi.where()
client = MongoClient("mongodb+srv://jominuk:alsdnr1549-@cluster0.pto4r2x.mongodb.net/?retryWrites=true&w=majority")
db = client.sparta

SECRET_KEY = 'tree'
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/main')
def main():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})

        return render_template('index.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

def login():
   return render_template('login.html')
@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/register')
def register():
   return render_template('register.html')

#################################
##  로그인을 위한 API             ##
#################################
@app.route('/user/login', methods=["POST"])
def user_login():
    user_email = request.form['email_give']
    user_password = request.form['password_give']

    pw_hash = hashlib.sha256(user_password.encode('utf-8')).hexdigest()

    result = db.user.find_one({'email': user_email, 'password': pw_hash})
    print(result)
    # print(user_password, user_email)

    if result is not None:

        payload = {
            'id': user_email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
        }
        print(payload)
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        print(token)
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 존재하지 않습니다.'})

@app.route('/user/register', methods=["POST"])
def user_register():
    username_receive = request.form['username_give']
    email_receive = request.form['email_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    print(username_receive, email_receive, pw_receive)
    db.user.insert_one({'email': email_receive, 'password': pw_hash, 'username': username_receive})

    return jsonify({'result': 'success'})

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
