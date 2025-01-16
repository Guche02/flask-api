from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")  # Replace with your connection URI
db = client["ToDoDB"]  # Replace with your DB name
user_collection = db["users"]  # Replace with your collection name

def insert_user(data):
    result = user_collection.insert_one(data)
    return str(result.inserted_id)

def get_user_by_id(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    return user

def update_user(user_id, update_data):
    result = user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    return result.modified_count

def delete_user(user_id):
    result = user_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count
