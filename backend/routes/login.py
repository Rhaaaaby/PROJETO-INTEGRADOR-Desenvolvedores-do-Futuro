from flask import Blueprint, request, jsonify
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash
from Models.user import User
from database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    Email = data.get("Email")
    Senha = data.get("Senha")

    if Email and Senha:
        user = User.query.filter_by(Email=Email).first()

        if user and check_password_hash(user.Senha, Senha):
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso!"}), 200
        
    return jsonify({"message": "credenciais inválidas!"}), 400