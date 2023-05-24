from flask import Flask, request, render_template, redirect, url_for, jsonify, session
import requests
from urllib import parse
import json
from pymongo import MongoClient
from config import *

app = Flask(__name__)

app.config.from_pyfile('config.py')

secret_key = app.config.get('SECRET_KEY', 'default_secret')

client = MongoClient(app.config["MONGODB_HOST"])

db = client[app.config["MONGODB_DATABASE"]]

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'login_status' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', login_status = session.get('login_status', False))

@app.route('/sotube', methods=['GET', 'POST'])
def about():
    return render_template('sotube.html')

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


@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method=="POST":
        collection = db['user_info']
        email = request.form['email']
        passwd = request.form['password']
        collection.insert_one({'email' : email, 'password' : passwd})
        return redirect(url_for('home'))

@app.route('/contact', methods=['POST'])
def contact():
    if request.method=="POST":
        collection = db['contact']
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        collection.insert_one({'name' : name, 'email' : email, 'password' : message})
        return redirect(url_for('home'))

        
@app.route("/email_check", methods=['POST'])
def email_check():
    if request.method == "POST":
        collection = db['user_info']
        email = request.json['email']
        user = collection.find_one({'email' : email})

        if user:
            return jsonify({'exists' : True})
        else:
            return jsonify({'exists' : False})
        
@app.route("/confirm_user", methods=['POST'])
def confirm_user():
    if request.method == "POST":
        collection = db['user_info']
        email = request.form.get('email')
        password = request.form.get('password')
        user = collection.find_one({'email' : email, 'password' : password})

        if user:
            session['login_status'] = True
            return jsonify({'message' : 'Login succeed'}), 200
        else:
            return jsonify({'message' : 'Invalid email or Password'}), 401
        


@app.route("/logout")
# @login_required
def logout():
    session.pop('login_status', None)
    return redirect(url_for('home'))

@app.route("/login_status")
def login_status():
    return jsonify({'login_status' : session.get("login_status", False)})

if __name__ == '__main__':
    app.run(port=5001)