from flask import Flask, request, render_template, redirect, url_for, jsonify, session
import json
from pymongo import MongoClient
from config import *

app = Flask(__name__)

from func import bp, login_required

app.register_blueprint(bp)

app.config.from_pyfile('config.py')

secret_key = app.config.get('SECRET_KEY', 'default_secret')

client = MongoClient(app.config["MONGODB_HOST"])

db = client[app.config["MONGODB_DATABASE"]]



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', login_status = session.get('login_status', False))

@app.route('/sotube', methods=['GET', 'POST'])
def about():
    return render_template('sotube.html', login_status = session.get('login_status', False))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if(session.get('login_status', False)):
        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if(session.get('login_status', False)):
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/mypage', methods=['GET', 'POST'])
@login_required
def mypage():
    return render_template('mypage.html')

@app.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    return render_template('feedback.html')




if __name__ == '__main__':
    # app.run(host = '0.0.0.0', port=5001)
    app.run(port=5001)