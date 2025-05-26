from flask import Blueprint, request, jsonify
from ..database import db
from ..Models.produto import Produto

produto_api = Blueprint('produto_api', __name__)

@produto_api.route('/produtos', methods=['POST'])
def criar_produto():
    data = request.get_json()

    try:
        novo_produto = Produto(
            Nome=data['Nome'],
            Descricao=data['Descricao'],
            Imagem_url=data['Imagem_url'],
            Estado=data['Estado'],
            Status=data['Status'],
            Cadastro_Produto_id_Cadastro_Produto=data['Cadastro_Produto_id_Cadastro_Produto'],
            Usuario_id_Usuario=data['Usuario_id_Usuario'],
            Categoria_id_Categoria=data['Categoria_id_Categoria']
        )

        db.session.add(novo_produto)
        db.session.commit()

        return jsonify({"mensagem": "Produto cadastrado com sucesso!", "id": novo_produto.id_Produto}), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 400