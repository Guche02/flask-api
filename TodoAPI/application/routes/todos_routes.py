from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity
from application.controllers.todo_controller import (
    view_todos,
    add_todos,
    delete_todo
)
from application.middleware.auth_middleware import auth_middleware

todos_routes = Blueprint("todos_routes", __name__)

@todos_routes.route("/view", methods=["GET"])
def view_todos_route():
    user_id = get_jwt_identity()  
    return view_todos(user_id)

@todos_routes.route("/add", methods=["PUT"])
def add_todos_route():
    user_id = get_jwt_identity() 
    return add_todos(request, user_id)

@todos_routes.route("/delete", methods=["PUT"])
def delete_todo_route():
    user_id = get_jwt_identity()  
    return delete_todo(request, user_id)
