from flask import Flask
from flask_pymongo import PyMongo

# Import routes (Ensure your user_route.py is inside the routes folder)
# from app.routes import user_route

def create_app():           
    # Initialize Flask app
    app = Flask(__name__)

    # Set up MongoDB URI
    app.secret_key = "secretkey"
    app.config['MONGO_URI'] = "mongodb://localhost:27017/User"

    mongo = PyMongo(app)
    # app.register_blueprint(user_route)

    return app
