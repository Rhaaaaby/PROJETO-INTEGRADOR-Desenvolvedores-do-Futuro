from flask_login import LoginManager
from .routes import init_app_routes
from .Models.user import User
from sqlalchemy import text
from .config import Config 
from .database import db
from flask import Flask
import mysql.connector
import os

# Configuração do Flask
app = Flask(
    __name__,
    static_folder=os.path.join("..", "frontend", "static"),
    template_folder=os.path.join("..", "frontend", "templates")
)

#Configurações
app.config.from_object(Config)

# Pasta de uploads
UPLOAD_FOLDER = os.path.join(app.root_path, '../static/uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Banco de Dados
db.init_app(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Rotas do projeto
init_app_routes(app)

# Conectar MySQL
def conectar_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="doa"
    )

# Rota teste do banco com SQLAlchemy
@app.route('/teste-db')
def teste_db():
    try:
        with db.engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
        return "Conexão com o banco funcionando."
    except Exception as e:
        return f"Conexão não estabelecida: {e}"

# Rota de teste simples
@app.route('/teste', methods=['GET'])
def teste():
    return "Hello World!"

# Iniciar servidor
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)