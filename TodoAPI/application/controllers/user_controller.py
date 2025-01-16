from flask import jsonify, request
from application.services.user_service import create_user, retrieve_user, modify_user, remove_user
from bson.json_util import dumps





