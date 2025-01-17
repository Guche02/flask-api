from application.services.user_service import (
    create_user, 
    login_user, 
    retrieve_user, 
    modify_user, 
    remove_user
)
from flask import jsonify

def create_user_controller(data):
    """
    Controller logic for creating a user. 
    Validates input and calls the service function to insert the user.
    """
    if not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing required fields"}), 400

    # Call the service function
    result = create_user(data)
    return jsonify(result), 201  # Return a response with HTTP 201 Created

def login_user_controller(data):
    """
    Controller logic for logging in a user.
    Validates the credentials and returns the login response.
    """
    if not data.get('email') or not data.get('password'):
        return jsonify({"error": "Email and password are required"}), 400

    # Call the service function
    result, status_code = login_user(data)
    return jsonify(result), status_code


def get_user_controller(user_id):
    """
    Controller logic for retrieving a user by ID.
    Handles errors if the user does not exist.
    """
    user = retrieve_user(user_id)
    if isinstance(user, dict) and user.get('error'):  
        return jsonify(user), 404

    # Convert the ObjectId to a string
    if '_id' in user:
        user['_id'] = str(user['_id'])

    return jsonify(user), 200

def update_user_controller(user_id, data):
    """
    Controller logic for updating user details.
    """
    if not data:
        return jsonify({"error": "No data provided for update"}), 400
    
    result = modify_user(user_id, data)
    if isinstance(result, dict) and result.get('error'):
        return jsonify(result), 404  # Return a 404 if user not found
    return jsonify(result), 200  # Return 200 for successful update

def delete_user_controller(user_id):
    """
    Controller logic for deleting a user by ID.
    """
    result = remove_user(user_id)
    if isinstance(result, dict) and result.get('error'):
        return jsonify(result), 404  # Return 404 if user not found
    return jsonify(result), 200  # Return 200 for successful deletion
