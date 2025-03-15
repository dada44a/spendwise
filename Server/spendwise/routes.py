from flask import Blueprint, jsonify, request
from models import db, User

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask App!"})

@routes.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@routes.route("/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = User(name=data["name"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully!"}), 201
