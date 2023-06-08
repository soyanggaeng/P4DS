from model.view import *
from model.cos import *
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from pymongo import MongoClient

class model():
    def __init__(self, df, inputs, budget):
        self.df = df.copy()
        self.m1 = view("/Users/jinwoo/Desktop/project/web/YAMP/model/randomforest.pkl", df)
        self.m2 = cos('/Users/jinwoo/Desktop/project/web/YAMP/model/model1_df.pkl', inputs[:])
        # self.m3 = pd.read_pickle("/Users/jinwoo/Desktop/project/web/YAMP/model/comment.pkl")
        self.budget = budget
        client = MongoClient('mongodb://localhost:27017/')
        db = client['sotube']
        cursor = db.comment_score.find({}, {"_id" : 0})
        comments = [doc for doc in cursor]
        comments = pd.DataFrame(comments)
        self.m3 = comments.copy()

    def predict(self):
        view = self.m1.predict()
        cos = self.m2.predict()
        comment = self.m3
        df = pd.merge(view,cos, on="유튜버", how = 'left')
        df = pd.merge(df, comment, on = "유튜버", how = "left")
        mm = MinMaxScaler()
        df['view_count_mm'] = mm.fit_transform(df[['view_count']])
        df['word_corr_mm'] = mm.fit_transform(df[['word_corr']])
        df['comment_analysis_score_mm'] = mm.fit_transform(df[['comment_analysis_score']])
        df['model_score'] = df['view_count_mm'] + df['word_corr_mm'] + df['comment_analysis_score_mm']
        # df['model_score'] = df['view_count_mm'] + 0.4*df['word_corr_mm'] + 0.4*df['comment_analysis_score_mm']


        df = df.loc[df['budget'] <= self.budget]
        df = df.sort_values(by='model_score', ascending=False)
        df_r = df[['유튜버', 'word_corr', 'comment_analysis_score']]
        self.view=view
        self.cos=cos
        self.comment=comment
        self.df2 = df
        return df_r

