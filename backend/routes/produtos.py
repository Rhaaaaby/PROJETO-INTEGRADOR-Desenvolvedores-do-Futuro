from flask import Blueprint, render_template
from ..Models import Produto

produtos_bp = Blueprint('feed', __name__)

@produtos_bp.route('/feed')
def feed():
    produtos = Produto.query.filter_by(status='disponivel').all()
    return render_template('doacoes.html', produtos=produtos)