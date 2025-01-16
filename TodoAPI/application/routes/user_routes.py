from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from application.services.user_service import create_user, retrieve_user, modify_user, remove_user

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/users", methods=["POST"])
def create_user_route():
    data = request.json
    result = create_user(data)
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

