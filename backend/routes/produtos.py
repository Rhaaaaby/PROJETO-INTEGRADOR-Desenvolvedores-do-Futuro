from flask import Blueprint, render_template
from ..Models.produto import Produto
from ..Models.categoria import Categoria

produtos_bp = Blueprint('feed', __name__)

@produtos_bp.route('/feed')
def feed():
    Produtos = Produto.query.filter_by(Status='disponivel').all()
    Categorias = Categoria.query.all()
    
    return render_template('doacoes.html', Produtos=Produtos, Categorias=Categorias, categorias_selecionadas=[])