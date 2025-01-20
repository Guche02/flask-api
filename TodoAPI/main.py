from flask import Flask, request
from flask_jwt_extended import JWTManager
from application.routes.user_routes import user_routes
from application.routes.todos_routes import todos_routes
from application.middleware.auth_middleware import auth_middleware

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key_here'  
jwt = JWTManager(app)

@app.before_request
def before_request():
    if request.path.startswith("/todos"):
        response = auth_middleware()
        if response:
            return response
        
app.register_blueprint(user_routes, url_prefix="/users")
app.register_blueprint(todos_routes, url_prefix="/todos")

if __name__ == "__main__":
    app.run(debug=True)
