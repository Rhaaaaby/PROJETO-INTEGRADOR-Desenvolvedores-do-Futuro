from ..database import db

class Categoria(db.Model):
    __tablename__ = 'Categoria'
    
    id_Categoria = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100), nullable=False)
    Descricao = db.Column(db.String(255), nullable=False)