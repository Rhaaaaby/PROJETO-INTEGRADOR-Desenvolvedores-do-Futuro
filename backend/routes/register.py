#rota criada para testes do login

from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from werkzeug.security import generate_password_hash
from ..Models.user import User
from ..database import db

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        Nome=request.form.get('Nome')
        Email=request.form.get('Email')
        Telefone=request.form.get('Telefone')
        Senha=request.form.get('Senha')
        senha_hash=generate_password_hash(Senha)
        Preferencia=request.form.get('Preferencia')
        Tipo_Conta=request.form.get('Tipo_Conta')

        #checando se o email já existe
        if User.query.filter_by(Email=Email).first():
            return render_template('register.html', error="Email já cadastrado!")
        
        novo_usuario = User(
            Nome= Nome,
            Email= Email,
            Telefone= Telefone,
            Senha= senha_hash,
            Preferencia= Preferencia,
            Tipo_Conta= Tipo_Conta
        )
    
        db.session.add(novo_usuario)
        db.session.commit()

        return render_template('register.html', success="Usuário cadastrado com sucesso!")
    return render_template('register.html')