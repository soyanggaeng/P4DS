from pymongo import MongoClient
from flask import g

def get_db():
    if 'db' not in g:
        g.db = MongoClient("mongodb://localhost:27017/")["sotube"]
    return g.db