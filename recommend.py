from flask import Blueprint, session, redirect, url_for, jsonify, request, g
# from pymongo import MongoClient
from config import *
import datetime
from func import login_required
from model.model import model

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