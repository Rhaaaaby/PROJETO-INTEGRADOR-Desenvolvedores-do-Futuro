from flask import Blueprint, render_template
from jinja2 import TemplateNotFound
from ..database import db
from flask_login import login_required, current_user, logout_user
from werkzeug.exceptions import abort
from ..Models.user import User
from flask import flash, redirect, url_for


minha_conta_bp = Blueprint('minha_conta', __name__)

# MINHA CONTA
    
@minha_conta_bp.route("/minha_conta")
def minha_conta():
    try:
        return render_template('MinhaConta.html', User=current_user)
    except TemplateNotFound:
        return "Template not found", 404
    
# deletar usuário

@minha_conta_bp.route('/deletar_usuario/<int:id_Usuario>', methods=['POST'])
@login_required
def deletar_usuario(id_Usuario):
    if current_user.id != id_Usuario:
        abort(403)  # proíbe deletar outro usuário

    usuario = User.query.get_or_404(id_Usuario)
    db.session.delete(usuario)
    db.session.commit()
    logout_user()
    flash('Usuário deletado com sucesso.', 'success')
    return redirect(url_for('home.home'))