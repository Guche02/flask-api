from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from werkzeug.exceptions import Unauthorized
from jwt.exceptions import ExpiredSignatureError

def auth_middleware():
    """Middleware to enforce JWT authentication."""
    try:
        # Verify the JWT in the request
        verify_jwt_in_request()

        # Retrieve the user ID from the token
        user_id = get_jwt_identity()

        # Check if user_id is None or invalid
        if not user_id:
            return jsonify({"error": "Unauthorized access: No user ID in the token."}), 401

    except ExpiredSignatureError:
        return jsonify({"error": "Token has expired. Please log in again."}), 401
    except Unauthorized as e:
        return jsonify({"error": f"Unauthorized access: {str(e)}"}), 401
    except Exception as e:
        return jsonify({"error": f"Unauthorized access: {str(e)}"}), 401
