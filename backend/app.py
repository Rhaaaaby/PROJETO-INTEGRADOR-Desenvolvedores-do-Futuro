from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_login import LoginManager
from config import Config 
from database import db
from Models.user import User
from routes import init_app_routes


app = Flask(__name__)

init_app_routes(app)

#Instanciando Config
app.config.from_object(Config)

#inicializando o login Manager
login_manager= LoginManager()
login_manager.init_app(app)

db.init_app(app)

login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/teste-db')
def teste_db():
    try:
        # Faz uma consulta simples só pra garantir que tá tudo ok
        with db.engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
        return "Conexão com o banco funcionando lindamente!"
    except Exception as e:
        return f"Deu ruim na conexão: {e}"


@app.route('/teste', methods=['GET'])
def teste():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)