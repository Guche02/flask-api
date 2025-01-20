from application.services.user_service import retrieve_user, modify_user

def get_user_todos(user_id):
    user = retrieve_user(user_id)
    if not user:
        return None
    return user.get("todolist", [])

def update_user_todos(user_id, new_todos):
    user = retrieve_user(user_id)
    if not user:
        return None

    current_todos = user.get("todolist", [])
    if current_todos is None:
        current_todos = []
    
    updated_todos = current_todos + new_todos
    modify_user(user_id, {"todolist": updated_todos})
    return {"todolist": updated_todos}

def delete_user_todo_by_index(user_id, index):
    user = retrieve_user(user_id)
    if not user:
        return {"error": "User not found"}

    current_todos = user.get("todolist", [])
    if index < 0 or index >= len(current_todos):
        return {"error": f"Index out of range. Valid range is 0 to {len(current_todos) - 1}."}

    deleted_item = current_todos.pop(index)
    modify_user(user_id, {"todolist": current_todos})
    return {
        "message": "Todo deleted successfully",
        "deleted_item": deleted_item,
        "updated_todolist": current_todos
    }
