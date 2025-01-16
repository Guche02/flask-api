from flask import Flask
from flask_jwt_extended import JWTManager
from application.routes.user_routes import user_routes

app = Flask(__name__)

# Set the secret key for JWT encoding/decoding
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key_here'  # Replace with a secure secret

# Initialize JWTManager with the app
jwt = JWTManager(app)

app.register_blueprint(user_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
