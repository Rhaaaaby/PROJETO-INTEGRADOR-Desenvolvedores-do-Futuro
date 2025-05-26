from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from ..database import db
from ..Models import cadastro_produto, produto, categoria

doacoes_bp= Blueprint("doacoes", __name__)

@doacoes_bp.route("/doações", methods=['GET', 'POST'])
def mostrar_doacoes(): 
    Produtos = produto.Produto.query.filter_by(Status='disponivel').all()
    Categorias = list({p.categoria for p in Produtos if p.categoria})

    return render_template(
        'doacoes.html',
        Produtos=Produtos,
        Categorias=Categorias
    )