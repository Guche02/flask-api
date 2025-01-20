from flask import jsonify
from application.services.todo_services import (
    get_user_todos,
    update_user_todos,
    delete_user_todo_by_index
)

def view_todos(user_id):
    todos = get_user_todos(user_id)
    if todos is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"todolist": todos}), 200

def add_todos(request, user_id):
    data = request.json.get("todolist", [])
    
    if not isinstance(data, list):
        return jsonify({"error": "Invalid data format. Expected a list of todos."}), 400

    updated_todos = update_user_todos(user_id, data)
    if updated_todos is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(updated_todos), 200

def delete_todo(request, user_id):
    index = request.json.get("index")
    
    if index is None or not isinstance(index, int):
        return jsonify({"error": "Invalid data format. Expected an integer index."}), 400

    result = delete_user_todo_by_index(user_id, index)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 400
    return jsonify(result), 200
