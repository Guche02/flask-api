from application.models.user_model import insert_user, get_user_by_id, update_user, delete_user

def create_user(data):
    user_id = insert_user(data)
    return {"message": "User created successfully", "user_id": user_id}

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
