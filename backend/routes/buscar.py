from flask import Blueprint, request, render_template

buscar_bp = Blueprint('buscar', __name__)

@buscar_bp.route('/buscar', methods=['GET'])
def buscar():
    termo = request.form.get('query', '').strip()
    categorias_selecionadas = request.form.getlist('categoria')
    
    # Lógica de filtragem (implemente depois)
    produtos_filtrados = []  # Substitua pela query real
    
    return render_template(
        'doacoes.html',
        produtos=produtos_filtrados,
        categorias=categorias_selecionadas
    )