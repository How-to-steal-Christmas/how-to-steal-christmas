from flask import Flask, render_template, jsonify, request, session, redirect, url_for
app = Flask(__name__)
import datetime

@app.route('/')
def home():
   return render_template('main.html')


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
        # '1mychk': today.strftme('%YY-%MM-%DD'),
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