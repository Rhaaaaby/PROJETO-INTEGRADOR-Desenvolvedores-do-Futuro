from datetime import datetime
from ..database import db

class Produto(db.Model):
    __tablename__ = 'Produto'

    id_Produto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nome = db.Column(db.String(100), nullable=False)
    Descricao = db.Column(db.String(255), nullable=False)
    Imagem_url = db.Column(db.String(255), nullable=False)
    Criado_em = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    Estado = db.Column(db.Enum('novo', 'semi-novo', 'usado', name='estado_enum'), nullable=False)
    Status = db.Column(db.Enum('disponivel', 'reservado', 'doado', name='status_enum'), nullable=False)
    
    #Chaves estrangeiras
    Cadastro_Produto_id_Cadastro_Produto = db.Column(db.Integer, db.ForeignKey('Cadastro_Produto.id_Cadastro_Produto'), nullable=False)
    Usuario_id_Usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_Usuario'), nullable=False)
    Categoria_id_Categoria = db.Column(db.Integer, db.ForeignKey('Categoria.id_Categoria'), nullable=False)
    
    #Relacionamentos
    cadastro_produto = db.relationship('CadastroProduto', backref='produtos')
    usuario = db.relationship('Usuario', back_populates='produtos')
    categoria = db.relationship('Categoria', back_populates='produtos')

    def __repr__(self):
        return f'<Produto {self.Nome}>'