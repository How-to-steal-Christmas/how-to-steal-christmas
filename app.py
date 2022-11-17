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

@app.route('/')
def home():
    return render_template('main.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)