from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user
from ..Models.user import User
from ..database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Email = request.form.get("Email")
        Senha = request.form.get("Senha")

        if Email and Senha:
            user = User.query.filter_by(Email=Email).first()

            if user and check_password_hash(user.Senha, Senha):
                login_user(user)
                flash('Login efetuado com sucesso!', 'sucess', current_user.is_authenticated)
                return redirect(url_for('home'))
            flash('Crendenciais inválidas!', 'error')
            return render_template('login.html') 
    return render_template('login.html')