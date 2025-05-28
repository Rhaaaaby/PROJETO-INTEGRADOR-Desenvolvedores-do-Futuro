from flask import Blueprint, request, render_template, flash, redirect, url_for
from ..Models.produto import Produto
from ..Models.categoria import Categoria
from ..database import db

doacoes_bp = Blueprint('doacoes', __name__)

@doacoes_bp.route('/doacoes', methods=['GET'])
def doacoes():

    categoria_id = request.args.get('categoria_id')
    termo = request.args.get('query', '').strip()

    # Query base: produtos disponíveis
    query = Produto.query.filter_by(Status='disponivel')

    # Filtra pelo termo no nome do produto (opcional)
    if termo:
        query = query.filter(Produto.Nome.ilike(f'%{termo}%'))

    # Filtra por categoria, se especificada
    if categoria_id:
        query = query.filter_by(Categoria_id_Categoria=categoria_id)

    produtos = query.order_by(Produto.id_Produto.desc()).all()

    categorias = Categoria.query.order_by(Categoria.Nome).all()

    return render_template(
        'doacoes.html',
        produtos=produtos,
        categorias=categorias,
        categoria_selecionada_id=int(categoria_id) if categoria_id else None,
        termo_busca=termo
    )