from flask import Flask
from application.routes.user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
