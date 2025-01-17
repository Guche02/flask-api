from flask import Blueprint, request, jsonify
from application.services.user_service import retrieve_user, modify_user
from flask_jwt_extended import jwt_required, get_jwt_identity  

todos_routes = Blueprint("todos_routes", __name__)

@todos_routes.route("/view", methods=['GET'])
@jwt_required()  
def view_todos_route():

    user_id = get_jwt_identity()
    user = retrieve_user(user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    todos = user.get('todolist', [])
    return jsonify({"todolist": todos}), 200

@todos_routes.route("/add", methods=['PUT'])
@jwt_required()
def update_todo_list():
    user_id = get_jwt_identity()
    user = retrieve_user(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json.get("todolist", [])
    
    if not isinstance(data, list):
        return jsonify({"error": "Invalid data format. Expected a list of todos."}), 400
    
    current_todos = user.get("todolist", [])
    if current_todos is None:
        current_todos = []
    updated_todos = current_todos + data
    result = modify_user(user_id, {"todolist": updated_todos})
    
    return jsonify(result)

@todos_routes.route("/delete", methods=['PUT'])
@jwt_required()
def delete_todo_by_index():
    user_id = get_jwt_identity()
    user = retrieve_user(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404
    index = request.json.get("index")
    
    if index is None or not isinstance(index, int):
        return jsonify({"error": "Invalid data format. Expected an integer index."}), 400

    current_todos = user.get("todolist", [])
    if index < 0 or index >= len(current_todos):
        return jsonify({"error": f"Index out of range. Valid range is 0 to {len(current_todos) - 1}."}), 400

    deleted_item = current_todos.pop(index)
    result = modify_user(user_id, {"todolist": current_todos})
    return jsonify({"message": "Todo deleted successfully", "deleted_item": deleted_item, "updated_todolist": current_todos})