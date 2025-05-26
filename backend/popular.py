from app import app
from database import db
from Models.produto import Produto
from Models.categoria import Categoria
from Models.user import User
from Models.cadastro_produto import Cadastro_Produto
from datetime import datetime

with app.app_context():
    # Criar Categoria
    categoria = Categoria(Nome='Roupas', Descricao='Roupas em geral')
    db.session.add(categoria)
    db.session.commit()

    # Criar CadastroProduto
    cadastro = Cadastro_Produto(Nome='Camisa', Descricao='Camisa preta')
    db.session.add(cadastro)
    db.session.commit()

    # Criar Usuário fake
    user = User(nome='Tester', email='teste@email.com', senha='123')
    db.session.add(user)
    db.session.commit()

    # Criar Produto
    produto = Produto(
        Nome='Camisa do Metallica',
        Descricao='Preta, tamanho G',
        Imagem_url='images/exemplo_produtos/metallica.png',
        Criado_em=datetime.utcnow(),
        Estado='usado',
        Status='disponivel',
        Cadastro_Produto_id_Cadastro_Produto=cadastro.id_Cadastro_Produto,
        Usuario_id_Usuario=user.id_Usuario,
        Categoria_id_Categoria=categoria.id_Categoria
    )
    db.session.add(produto)
    db.session.commit()

    print("Banco populado com sucesso!")