from flask import Blueprint, session, redirect, url_for, jsonify, request, g, send_from_directory
# from pymongo import MongoClient
from config import *
import datetime
from func import login_required
from model.model import model
from model.word_cloud import wc_plot
import json
import pandas as pd
from model.cos import cos
# client = MongoClient(MONGODB_HOST)

# db = client[MONGODB_DATABASE]

bp2 = Blueprint("recommend_blueprint", __name__);


@bp2.route("/getRecommendedChannels", methods=['POST'])
@login_required
def getRecommendedChannels():
    if request.method == 'POST':
        L = g.db['youtuber_list'].find_one()['youtuber_list']
        query = {"title": {"$in": L}}
        projection = {"_id": 0, "title" : 1, "category" : 1, "subscriberCount" : 1}  # Exclude the _id field if desired

        results = g.db['channel_info'].find(query, projection)
        lists = []
        for doc in results:
            lists.append(doc)
        df = pd.DataFrame(lists)
        new_key = {'title' : '유튜버',
                'category' : 'category',
                'subscriberCount' : 'subscriber_count'}
        df = df.rename(columns=new_key)

        product = request.form.get('product')
        df['product_category'] = product
        budget = int(request.form.get('budget'))
        keywords = []
        for i in range(3):
            if(f'keyword-{i}' in request.form.to_dict()):
                keywords.append(request.form.get(f'keyword-{i}'))

        m = model(df, keywords, budget)
        youtubers = m.predict()

        return jsonify(youtubers.to_dict(orient='records')[:50])
    
@bp2.route("/channelAnalysis", methods=['POST'])
@login_required
def channelAnalysis():
    if request.method == 'POST':
        channel = request.json['channel']
        wc_plot(channel)
        d = {'channel' : channel, 'msg' : 'succeeded'}
        return jsonify(d)
    
@bp2.route("/keywordAnalysis", methods=['POST'])
@login_required
def keywordAnalysis():
    if request.method == 'POST':
        inputs = request.json['keyword'].split(',')
        m = cos('/Users/jinwoo/Desktop/project/web/YAMP/model/model1_df.pkl', inputs)
        df = m.predict()
        df = df.sort_values(by='word_corr', ascending=False)
        youtuber_list = list(df['유튜버'])[:5]
        # product = request.form.get('product')
        # budget = request.form.get('budget')
        # keywords = request.form.get('keywords')
        # m = model(product, budget, keywords)
        # youtubers = m.predict()

        return jsonify(youtuber_list)
    
# @bp2.route('/image/<filename>')
# @login_required
# def image(filename):
#     image_folder = './static/img'
#     return send_from_directory(image_folder, filename)
    

# @bp2.route("/test", methods=['POST'])
# @login_required
# def test():
#     if request.method == 'POST':
#         with open("test.json", "r") as f:
#             L = json.load(f)

#         return jsonify(L)
    

