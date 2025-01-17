from pymongo import MongoClient
from bson.objectid import ObjectId

from application.utils.security import hash_password

client = MongoClient("mongodb://localhost:27017/")  
db = client["ToDoDB"]  
user_collection = db["users"]  

def insert_user(data):
     """Create a new user and hash the password."""

     name = data.get("name")
     email = data.get("email")
     password = data.get("password")  
     age = data.get("age")
     todolist = data.get("todolist")

     if not all([name, email, password]):
        return {"error": "Missing required fields: name, email, password"}, 400

     hashed_password = hash_password(password)

     user = {
        "name": name,
        "email": email,
        "password": hashed_password, 
        "age": age,
        "todolist": todolist
    }

     result = db.users.insert_one(user)
     return str(result.inserted_id)

def get_user_by_email(email):
    user = user_collection.find_one({"email": email})  
    return user

def get_user_by_id(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    return user

def update_user(user_id, update_data):
    result = user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    return result.modified_count

def delete_user(user_id):
    result = user_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count
