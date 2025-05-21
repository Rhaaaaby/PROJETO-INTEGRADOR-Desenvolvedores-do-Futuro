from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .routes import init_app_routes
from .Models.user import User
from sqlalchemy import text
from .config import Config 
from .database import db
from flask import Flask
import os

app = Flask(
    __name__,
    static_folder=os.path.join("..", "frontend", "static"),
    template_folder=os.path.join("..", "frontend", "templates")
)

#Configurações
app.config.from_object(Config)

#Banco de Dados
db.init_app(app)

#Login Manager
login_manager= LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

#Rotas
init_app_routes(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/teste-db')
def teste_db():
    try:
        # Faz uma consulta simples só pra garantir que tá tudo ok
        with db.engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
        return "Conexão com o banco funcionando."
    except Exception as e:
        return f"Conexão não estabelecida: {e}"

@app.route('/teste', methods=['GET'])
def teste():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)