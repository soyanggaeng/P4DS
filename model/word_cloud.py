from wordcloud import WordCloud
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import pandas as pd

# 유튜버 이름 넣으면 word cloud 보여줌
def wc_plot(name):
    yc = pd.read_pickle("yc.pickle")
    s = yc.loc[yc['유튜버'] == name]
    okt = Okt()
    nouns = okt.nouns(' '.join(s['Comment']))
    words = nouns

    wordcloud = WordCloud(font_path = './NanumGothic-Regular.ttf', width=800, height=800, background_color='white', min_font_size=10).generate(' '.join(words))
    plt.figure(figsize=(12, 12), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()