from mongoengine import Document, StringField, IntField, ListField, connect
from application.utils.security import hash_password

connect("ToDoDB", host="mongodb://localhost:27017/")

class User(Document):
    name = StringField(required=True, max_length=100)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    age = IntField()
    todolist = ListField(StringField())

    meta = {"collection": "users"}  # Map this model to the "users" collection

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
    try:
        user = User(
            name=name,
            email=email,
            password=hashed_password,
            age=age,
            todolist=todolist
        )
        user.save() 
        return {"message": "User created successfully", "user_id": str(user.id)}
    except Exception as e:
        return {"error": str(e)}, 500

def get_user_by_email(email):
    """Retrieve a user by email."""
    user = User.objects(email=email).first()  
    if user:
        return user.to_mongo().to_dict()  

def get_user_by_id(user_id):
    """Retrieve a user by ID."""
    try:
        user = User.objects(id=user_id).first()  
        if user:
            return user.to_mongo().to_dict()  
        return None
    except Exception as e:
        return {"error": str(e)}, 400

def update_user(user_id, update_data):
    """Update a user's details."""
    try:
        user = User.objects(id=user_id).first()
        if not user:
            return {"error": "User not found"}, 404
        user.update(**update_data)  
        return {"message": "User updated successfully"}
    except Exception as e:
        return {"error": str(e)}, 400

def delete_user(user_id):
    """Delete a user by ID."""
    try:
        user = User.objects(id=user_id).first()
        if not user:
            return {"error": "User not found"}, 404
        user.delete() 
        return {"message": "User deleted successfully"}
    except Exception as e:
        return {"error": str(e)}, 400
