from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from ..database import db
from ..Models import cadastro_produto, produto, categoria

doacoes_bp= Blueprint("doacoes", __name__)

@doacoes_bp.route("/doações", methods=['GET', 'POST'])
def Produtos(): 
    return "Prestou"