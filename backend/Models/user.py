from database import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'Usuario'

    id_Usuario = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(50), unique=True, nullable=False)
    Telefone = db.Column(db.String(20), nullable=False)
    Senha = db.Column(db.String(255), nullable=False)
    Preferencia = db.Column(db.Enum('Troca', 'Doação', 'Receber Doação'), nullable=False)
    Tipo_Conta = db.Column(db.Enum('Pessoal', 'ONG', 'Instituição'), nullable=False)

    def get_id(self):
        return str(self.id_Usuario)