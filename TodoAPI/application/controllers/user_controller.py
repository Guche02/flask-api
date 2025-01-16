from flask import jsonify, request
from application.services.user_service import add_user_to_db

def add_user(mongo):
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    # Call the service to add the user to the DB
    user_id = add_user_to_db(mongo, _name, _email, _password)
    resp = jsonify({"message": "User added successfully", "user_id": str(user_id)})

    resp.status_code = 200
    return resp
