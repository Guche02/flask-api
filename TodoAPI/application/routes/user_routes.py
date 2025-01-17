from flask import Blueprint, request, jsonify
from application.controllers.user_controller import (
    create_user_controller, 
    login_user_controller, 
    get_user_controller, 
    update_user_controller, 
    delete_user_controller
)

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/register", methods=["POST"])
def create_user_route():
    data = request.json
    return create_user_controller(data)

@user_routes.route("/login", methods=["POST"])
def login_route():
    data = request.json
    return login_user_controller(data)

@user_routes.route("/<user_id>", methods=["GET"])
def get_user_route(user_id):
    return get_user_controller(user_id)

@user_routes.route("/<user_id>", methods=["PUT"])
def update_user_route(user_id):
    data = request.json
    return update_user_controller(user_id, data)

@user_routes.route("/<user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    return delete_user_controller(user_id)