from wordcloud import WordCloud
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import pandas as pd

# 유튜버 이름 넣으면 word cloud 보여줌
def wc_plot(name):
    yc = pd.read_pickle("/Users/jinwoo/Desktop/project/web/YAMP/model/yc.pkl")
    s = yc.loc[yc['유튜버'] == name]

    wordcloud = WordCloud(font_path = '/Users/jinwoo/Desktop/project/web/YAMP/model/NanumGothic-Regular.ttf', width=800, height=800, background_color='white', min_font_size=10).generate(' '.join(s['nouns']))
    # plt.figure(figsize=(12, 12), facecolor=None)
    # plt.imshow(wordcloud)
    # plt.axis("off")
    # plt.tight_layout(pad=0)
    wordcloud.to_file("/Users/jinwoo/Desktop/project/web/YAMP/static/img/wordcloud.png")