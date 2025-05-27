from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/<pagina>')
def render_paginas(pagina):
    try:
        return render_template(f'{pagina}.html')
    except:
        return "Página não encontrada", 404