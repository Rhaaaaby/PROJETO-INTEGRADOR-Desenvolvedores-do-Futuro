from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from ..Models.user import User
from ..database import db

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            form_data = {
                'Nome': request.form.get('Nome'),
                'Email': request.form.get('Email'),
                'Telefone': request.form.get('Telefone'),
                'Senha': request.form.get('Senha'),
                'Preferencia': request.form.get('Preferencia'),
                'Tipo_Conta': request.form.get('Tipo_Conta')
            }

            if not all(form_data.values()):
                flash('Todos os campos precisam ser preenchidos!', 'error')
                return render_template('register.html')

            #checando se o email já existe
            if User.query.filter_by(Email=form_data['Email']).first():
                flash('Email já cadastrado!', 'error')
                return render_template('register.html')
            
            novo_usuario = User(
                Nome=form_data['Nome'],
                Email=form_data['Email'],
                Telefone=form_data['Telefone'],
                Senha=generate_password_hash(form_data['Senha']),
                Preferencia=form_data['Preferencia'],
                Tipo_Conta=form_data['Tipo_Conta']
            )
        
            db.session.add(novo_usuario)
            db.session.commit()

            flash('Usuário cadastrado com sucesso!', 'sucess')
            #lembrar de adicionar a página home corretamente quando for feito o merge
            #return render_template(url_for('home.html'))

        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao cadastrar {str(e)}', 'error')
            return render_template('register.html')
    
    return render_template('register.html')
    