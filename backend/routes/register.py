#rota criada para testes do login

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from database import db
from Models.user import User

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Checando se o email já existe
    if User.query.filter_by(Email=data['Email']).first():
        return jsonify({"error": "Email já cadastrado!"}), 400

    novo_usuario = User(
        Nome=data['Nome'],
        Email=data['Email'],
        Telefone=data['Telefone'],
        Senha=generate_password_hash(data['Senha']),
        Preferencia=data['Preferencia'],
        Tipo_Conta=data['Tipo_Conta']
    )

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso!"}), 201