from flask import Flask
# from flask_pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e74dd52524b5d867a91e47b90ecdfa'
# app.config['MONGO_URI'] = 'mongodb+srv://Badhani:sparta@cluster0.l2e4sqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
uri = 'mongodb+srv://Badhani:sparta@cluster0.l2e4sqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
mongo_client = MongoClient(uri)
db = mongo_client.TODO

from application import route