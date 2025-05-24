from ..database import db

class CadastroProduto(db.Model):
    __tablename__ = 'Cadastro_Produto'
    
    id_Cadastro_Produto = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100), nullable=False)
    Descricao = db.Column(db.String(255), nullable=False)