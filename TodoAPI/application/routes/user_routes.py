from flask import Blueprint, request, jsonify
from application.services.user_service import create_user, retrieve_user, modify_user, remove_user, login_user
from bson.json_util import dumps
from flask_jwt_extended import jwt_required, get_jwt_identity  # Import necessary functions

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/register", methods=["POST"])
def create_user_route():
    data = request.json
    result = create_user(data)
    return jsonify(result)

@user_routes.route("/login", methods=["POST"])
def login_route():
    data = request.json
    result = login_user(data)
    return jsonify(result)

@user_routes.route("/users/<user_id>", methods=["GET"])
def get_user_route(user_id):
    user = retrieve_user(user_id)
    if user:
        return dumps(user)  # Automatically serializes ObjectId
    return jsonify({"error": "User not found"}), 404

@user_routes.route("/users/<user_id>", methods=["PUT"])
def update_user_route(user_id):
    data = request.json
    result = modify_user(user_id, data)
    return jsonify(result)

@user_routes.route("/users/<user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    result = remove_user(user_id)
    return jsonify(result)

@user_routes.route("/todos", methods=['GET'])
@jwt_required()  
def view_todos_route():

    user_id = get_jwt_identity()
    user = retrieve_user(user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    todos = user.get('todolist', [])
    
    return jsonify({"todos": todos}), 200