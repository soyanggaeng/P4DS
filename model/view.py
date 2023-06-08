import pickle
import pandas as pd
import numpy as np

class view():
    def __init__(self, m, df):
        with open(m, "rb") as f:
            self.m = pickle.load(f)
        self.df = df.copy()
        self.preprosessing()
        self.X = self.df[['paid_advertised', 'category', 'subscriber_count', 'date_difference','product_category']]
            
    def predict(self):
        self.df['view_count'] = self.m.predict(self.X)
        df = self.df[['유튜버', 'view_count', 'budget']]
        # df.loc[df['budget'] <= self.budget]
        return df
        
    
    def preprosessing(self):
        self.df['paid_advertised'] = 1
        self.df['date_difference'] = 20
        self.df['budget'] = self.df['subscriber_count'].apply(self.get_budget)
        
        category_labels = {
            'FOOD': 1,
            'TECH': 2,
            'INFO': 3,
            'BEAUTY': 4,
            'FILM': 5,
            'FASHION': 6,
            'PET': 7,
            'FUN': 8,
            'TRAVEL': 9,
            'ECONOMY': 10,
            'ENTN': 11,
            'GAME': 12,
            'CAR': 13,
            'LIFE': 14,
            'SPORTS': 15
        }

        product_categories = [
            'Beauty and Fashion',
            'Technology',
            'Automotive',
            'Entertainment and Media',
            'Travel and Tourism',
            'Home and Lifestyle',
            'Food and Beverage',
            'Gaming',
            'Financial Services',
            'Health and Fitness',
            'ntertainment and Media']
        category_to_number = {category: number for number, category in enumerate(product_categories)}

        self.df['category'] = self.df['category'].map(category_labels)
        self.df['product_category'] = self.df['product_category'].map(category_to_number)

        
    def get_budget(self, value):
        if value <= 50000:
            return 500
        elif value <= 100000:
            return 1000
        elif value <= 120000:
            return 1200
        elif value <= 150000:
            return 1300
        elif value <= 170000:
            return 1500
        elif value <= 200000:
            return 2000
        elif value <= 400000:
            return 3000
        elif value <= 600000:
            return 3500
        elif value <= 800000:
            return 4000
        elif value <= 1000000:
            return 4500
        elif value <= 1500000:
            return 5000
        elif value <= 3000000:
            return 6000