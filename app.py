from flask import Flask, request, render_template
import requests
from urllib import parse
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/sotube', methods=['GET', 'POST'])
def about():
    return render_template('sotube.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
# @app.route('/result', methods=['GET', 'POST'])
# def result():
#     if request.method=="POST":
#         summoner_name = request.form['summoner_name']
#         dt_obj = data.lol_api(summoner_name)
#         dt = dt_obj.allData()

#         return render_template('result.html', user_data=json.dumps(dt));


app.run(port=5001, debug=True)