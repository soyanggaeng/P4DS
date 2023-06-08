import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline


tokenizer = AutoTokenizer.from_pretrained("monologg/koelectra-base-v3-discriminator")

class cos():
    def __init__(self, data, inputs):
        self.data = pd.read_pickle(data)
        self.inputs = inputs[:]
        self.pre()
        
    def cos_similar(self):
        answers = []
        outputs = self.data['outputs'].to_list()
        inputs = self.data['inputs'].to_list()
        for i in range(len(outputs)):
            cosine_totals = []
            output_vec = outputs[i]
            for j in range(len(inputs[0])):
                input_vec = inputs[i][j]
                # print(input_vec)
                # print(output_vec)
                similarity = cosine_similarity([input_vec], [output_vec])[0][0]
                cosine_totals.append(similarity)
            ans = np.mean(cosine_totals)
            answers.append(ans)
        return answers
    
    def token(self, comment):
        inputs = tokenizer(comment, return_tensors="pt", padding=True, truncation=True, max_length=20).to("cpu")
        vector_inputs = inputs['input_ids'].numpy().flatten()
        vector_inputs = np.pad(vector_inputs, (0, 20 - len(vector_inputs)))
        return vector_inputs

    def preprocessing(self, word):
        word = word.replace(' ', '')
        word = word.split('#')
        word = ' '.join([str(words) for words in word])
        return word
    
    def pre(self):
        df = self.data
        df['word_analysis'] = (df['더보기란']).astype(str).apply(self.preprocessing)
        df['word_analysis'] = df['word_analysis'].dropna()
        df['outputs'] = df['word_analysis'].apply(self.token)
        s = []
        for word in self.inputs:
            s.append(self.token(word))
        df['inputs'] = [s]*len(df)
        self.data = df
        
    def predict(self):
        self.data['word_corr'] = self.cos_similar()
        ret_df = self.data.groupby('유튜버')['word_corr'].mean().reset_index()
        return ret_df