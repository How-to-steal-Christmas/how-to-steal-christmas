import certifi
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import jwt
import datetime
import hashlib
app = Flask(__name__)

from pymongo import MongoClient
ca = certifi.where()
# DB info

SECRET_KEY = 'tree'
@app.route('/')
def home():
    return render_template("home.html")

def login():
   return render_template('login.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/register')
def register():
   return render_template('register.html')

@app.route('/treeforguest')
def treeforguest():
   return render_template('treeforguest.html')

@app.route('/treeforuser')
def treeforuser():
   return render_template('treeforuser.html')

@app.route('/main')
def main():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})

        return render_template('mycalendars.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

#################################
##    Login , Register API     ##
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
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
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

#################################
## createtree, mycalendar API  ##
#################################
@app.route("/createtree", methods=["POST"])
def create_tree():
    calendar_list = list(db.calendar.find({}, {'_id': False}))
    count = len(calendar_list)

    today_receive = request.form['today_give']
    email_receive = request.form['email_give']
    user_name_receive = request.form['user_name_give']
    calendar_receive = request.form['calendar_name_give']
    file_receive = request.form['file_give']
    url_receive = request.form['url_give']
    coupon_receive = request.form['coupon_give']
    comment_receive = request.form['comment_give']
    create_time_receive = request.form['create_time_give']

    print(create_time_receive, today_receive)

    doc = {
        'idx': count,
        'today': today_receive,
        'email': email_receive,
        'user_name': user_name_receive,
        'calendar_name': calendar_receive,
        'create_time': create_time_receive,
        'item': [
            {
                'date': '2022-11-14',
                'file': file_receive,
                'url': url_receive,
                'coupon': coupon_receive,
                'comment': comment_receive
            },
            {
                'date': '2022-11-15',
                'file': file_receive,
                'url': url_receive,
                'coupon': coupon_receive,
                'comment': comment_receive
            },
            {
                'date': '2022-11-16',
                'file': file_receive,
                'url': url_receive,
                'coupon': coupon_receive,
                'comment': comment_receive
            },
            {
                'date': '2022-11-17',
                'file': file_receive,
                'url': url_receive,
                'coupon': coupon_receive,
                'comment': comment_receive
            },
            {
                'date': '2022-11-18',
                'file': file_receive,
                'url': url_receive,
                'coupon': coupon_receive,
                'comment': comment_receive
            },
            {
                'date': '2022-11-19',
                'file': file_receive,
                'url': url_receive,
                'coupon': coupon_receive,
                'comment': comment_receive
            },
            {
                'date': '2022-11-20',
                'file': file_receive,
                'url': url_receive,
                'coupon': coupon_receive,
                'comment': comment_receive
            }
        ]
    }

    db.calendar.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

@app.route("/mycalendars", methods=["GET"])
def calendar_get():
    # email_receive = request.form['email']
    calendar_list = list(db.calendar.find({}, {'_id': False}))
    return jsonify({'calendar': calendar_list})

@app.route("/mycalendars/delete", methods=["POST"])
def calendar_delete():
    idx_receive = request.form['idx_give']
    mail_receive = request.form['mail_give']
    user_name_receive = request.form['user_name_give']

    db.calendar.delete_one({'idx': int(idx_receive)})
    return jsonify({'msg': '삭제 완료!'})

@app.route("/mycalendars/edit/calendar", methods=["POST"])
def calendar_edit():
    idx_receive = request.form['idx_give']
    calendar_name_receive = request.form['calendar_name_give']

    db.calendar.update_one({'idx': int(idx_receive)}, {'$set': {'calendar_name': calendar_name_receive}})
    return jsonify({'msg': '수정 완료!'})

#################################
##         createcards API     ##
#################################
@app.route("/createcards", methods=["POST"])
def cards_post():
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

#################################
##           tree API          ##
#################################
@app.route('/tree/details', methods=['GET'])
def modal_data_get():
    calendar = request.args.get('calendar_name')
    print('calendar', calendar)
    modals = db.calendar.find_one({'calendar_name': calendar}, {'_id':False})
    print(modals)
    return jsonify({'modals': modals})

#################################
##    createcards API          ##
#################################
@app.route("/createcards/detail", methods=["POST"])
def modal_post():
   url_receive = request.form['url_give']
   coupon_receive = request.form['coupon_give']
   comment_receive = request.form['comment_give']
   calendar_receive = request.form['calendar_name']

   idx_receive = request.form['idx']
    
   # db.calendar.update_one({'calendar_name': calendar_receive}, {'$set': 'item'[idx_receive][{'url': url_receive, 'coupon': coupon_receive, 'comment': comment_receive}]})

   return jsonify({'msg':'선물 등록!'})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)