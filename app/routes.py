# app/routes.py

from flask import Blueprint, request, jsonify
from . import db
from .models import ExpanseTracker, LoginUser, Expanses

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    user = ExpanseTracker(name = data.get("name"),
                          email = data.get("email"),
                          password = data.get("password"))
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully!"}), 201

@main_bp.route("/get-user", methods=["GET"])
def get_users():
    users = ExpanseTracker.query.all()
    return jsonify([u.to_dict() for u in users]), 200

@main_bp.route("/delete-user", methods=["POST"])
def delete_user():
    email = request.get_json()

    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Retrieve the user from ExpanseTracker
    user = ExpanseTracker.query.filter_by(email=email).first()
    if user:
        db.session.delete(user)

    # Retrieve the user from LoginUser
    login_user = LoginUser.query.filter_by(email=email).first()
    if login_user:
        db.session.delete(login_user)

    db.session.commit()
    return jsonify({"message": "User deleted successfully!"}), 200

@main_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = ExpanseTracker.query.filter_by(
        name=data.get("name"), password=data.get("password")
    ).first()
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    LoginUser.query.delete()
    login_user = LoginUser(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.session.add(login_user)
    db.session.commit()

    return jsonify({
        "message": "Login successful!",
        "user": {"name": user.name, "email": user.email}
    }), 200

@main_bp.route("/get-login-user", methods=["GET"])
def get_login_user():
    logged_in = LoginUser.query.all()
    return jsonify([u.to_dict() for u in logged_in]), 200

@main_bp.route("/delete-login-user", methods=["GET"])
def delete_login_user():
    LoginUser.query.delete()
    db.session.commit()
    return jsonify({"message": "Login user deleted successfully!"}), 200

@main_bp.route("/add-expanse", methods=["POST"])
def add_expense():
    data = request.get_json()
    expense = Expanses(title = data.get("title"),
                      earn = data.get("earn"),
                      spend = data.get("spend"),
                      totalBalance = data.get("totalBalance"),
                      email = data.get("email"))
    db.session.add(expense)
    db.session.commit()
    return jsonify({"message": "Expense added successfully!"}), 201

@main_bp.route("/get-expanses", methods=["GET"])
def get_expanses():
    expanses = Expanses.query.all()
    return jsonify([e.to_dict() for e in expanses]), 200

@main_bp.route("/remove-expanses", methods=["POST"])
def remove_expense():
    data = request.get_json()
    exp = Expanses.query.filter_by(id=data).first()  # Correct comparison
    if not exp:
        return jsonify({"message": "Expense not found!"}), 404

    db.session.delete(exp)
    db.session.commit()
    return jsonify({"message": "Expense removed successfully!"}), 200


@main_bp.route("/reset-app", methods=["GET"])
def resetApp():
    db.session.query(ExpanseTracker).delete()
    db.session.query(LoginUser).delete()
    db.session.query(Expanses).delete()
    db.session.commit()

    return jsonify({"message": "Full app has been reset"}) 