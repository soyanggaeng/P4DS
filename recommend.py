from flask import Blueprint, session, redirect, url_for, jsonify, request, g
# from pymongo import MongoClient
from config import *
import datetime
from func import login_required
from model.model import model
import json
# client = MongoClient(MONGODB_HOST)

# db = client[MONGODB_DATABASE]

bp2 = Blueprint("recommend_blueprint", __name__);


@bp2.route("/getRecommendedChannels", methods=['POST'])
@login_required
def getRecommendedChannels():
    if request.method == 'POST':
        product = request.form.get('product')
        budget = request.form.get('budget')
        keywords = request.form.get('keywords')
        m = model(product, budget, keywords)
        youtubers = m.predict()

        return jsonify(youtubers)
    
@bp2.route("/channelAnalysis", methods=['POST'])
@login_required
def channelAnalysis():
    if request.method == 'POST':
        # product = request.form.get('product')
        # budget = request.form.get('budget')
        # keywords = request.form.get('keywords')
        # m = model(product, budget, keywords)
        # youtubers = m.predict()
        path = "static/img/word_ex.png"

        return jsonify({'path' : path})
    
@bp2.route("/keywordAnalysis", methods=['POST'])
@login_required
def keywordAnalysis():
    if request.method == 'POST':
        # product = request.form.get('product')
        # budget = request.form.get('budget')
        # keywords = request.form.get('keywords')
        # m = model(product, budget, keywords)
        # youtubers = m.predict()

        return jsonify(['유소나', '유지니 u genie', '유튜브 지식 쇼츠', '예술의 이유', '유백합 kkubi99'])

@bp2.route("/test", methods=['POST'])
@login_required
def test():
    if request.method == 'POST':
        with open("test.json", "r") as f:
            L = json.load(f)

        return jsonify(L)
    

