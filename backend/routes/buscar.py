from flask import Blueprint, request, render_template
from ..Models.produto import Produto

buscar_bp = Blueprint('buscar', __name__)

@buscar_bp.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('query', '').strip()
    categorias_selecionadas = request.args.getlist('Categoria')

    Produtos_query = Produto.query.filter_by(Status='disponivel')

    if termo:
        Produtos_query = Produtos_query.filter(Produto.nome.ilike(f'%{termo}%'))

    if categorias_selecionadas:
        Produtos_query = Produtos_query.filter(Produto.categoria.in_(categorias_selecionadas))
    
    produtos_filtrados = Produtos_query.all()

    todas_categorias = list({p.categoria for p in Produto.query.all()})
    
    return render_template(
        'doacoes.html',
        produtos=produtos_filtrados,
        categorias= todas_categorias,
        categorias_selecionadas=categorias_selecionadas
    )