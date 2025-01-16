from application.models.user_model import insert_user, get_user_by_id, update_user, delete_user, get_user_by_email
from flask_jwt_extended import create_access_token
from application.controllers.security import verify_password

def create_user(data):
    user_id = insert_user(data)
    return {"message": "User created successfully", "user_id": user_id}

def login_user(data):
    """
    This function handles the login process. It checks if the email exists and if
    the password is correct. If so, it returns a JWT token.
    """
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return {"error": "Email and password are required"}, 400
    
    user = get_user_by_email(email)
    
    if not user:
        return {"error": "User not found"}, 404
    
    if not verify_password(password, user['password']):
        return {"error": "Invalid password"}, 401

    access_token = create_access_token(identity=str(user['_id']))  

    return {
        "message": "Login successful",
        "access_token": access_token
    }, 200

def retrieve_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return user
    return {"error": "User not found"}

def modify_user(user_id, data):
    updated_count = update_user(user_id, data)
    if updated_count:
        return {"message": "User updated successfully"}
    return {"error": "User not found or no changes made"}

def remove_user(user_id):
    deleted_count = delete_user(user_id)
    if deleted_count:
        return {"message": "User deleted successfully"}
    return {"error": "User not found"}

