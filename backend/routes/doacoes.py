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

from flask import request, redirect, url_for, flash, render_template

@doacoes_bp.route('/reservar/<int:id_Produto>', methods=['POST'])
def reservar_produto(id_Produto):
    produto = Produto.query.get(id_Produto)
    if not produto:
        flash('Produto não encontrado.', 'error')
        return redirect(url_for('doacoes.doacoes'))

    if produto.reservado:
        flash('Produto já foi reservado.', 'warning')
        return redirect(url_for('doacoes.doacoes'))

    produto.reservado = True
    db.session.commit()
    flash(f'Produto "{produto.nome}" reservado com sucesso! 🎉', 'success')
    return redirect(url_for('doacoes.doacoes'))

@doacoes_bp.route('/feed')
def feed():
    produtos = Produto.query.filter_by(reservado=False).all()
    return render_template('doacoes.html', produtos=produtos)
