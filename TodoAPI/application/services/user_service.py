from application.models.user_model import (
    insert_user, 
    get_user_by_id, 
    update_user, 
    delete_user, 
    get_user_by_email
)
from flask_jwt_extended import create_access_token
from application.utils.security import verify_password
from application.services.event_service import log_new_user_event



def create_user(data):
    """
    Service function to create a new user and return the user ID.
    """
    user_id = insert_user(data)
    log_new_user_event(data)
    return {"message": "User created successfully", "user_id": user_id}

def login_user(data):
    """
    Service function for logging in a user by validating their email and password.
    Returns the access token on successful login.
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
    """
    Service function to retrieve a user by their user_id.
    """
    user = get_user_by_id(user_id)
    if user:
        return user
    return {"error": "User not found"}

def modify_user(user_id, data):
    """
    Service function to update user information.
    """
    updated_count = update_user(user_id, data)
    if updated_count:
        return {"message": "User updated successfully"}
    return {"error": "User not found or no changes made"}

def remove_user(user_id):
    """
    Service function to delete a user by user_id.
    """
    deleted_count = delete_user(user_id)
    if deleted_count:
        return {"message": "User deleted successfully"}
    return {"error": "User not found"}
