from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["software_aging"]

collection = db["metrics"]
alerts_collection = db["alerts"]