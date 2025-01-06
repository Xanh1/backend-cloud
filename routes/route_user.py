from flask import Blueprint, make_response, jsonify

url_user = Blueprint('url_user', __name__)

users = [
    {"id": 1, "name": "Juan", "email": "juan@example.com"},
    {"id": 2, "name": "Maria", "email": "maria@example.com"},
    {"id": 3, "name": "Carlos", "email": "carlos@example.com"}
]

@url_user.route('/users', methods = ['GET'])
def get_users():
    return make_response(jsonify(users), 200)