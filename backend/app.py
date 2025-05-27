from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.utils import secure_filename
from .routes import init_app_routes
from .Models.user import User
from sqlalchemy import text
from .config import Config 
from .database import db
import mysql.connector
import os

#Mesclando dois arquivos app.py das branches Rhaaby e antonio

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        foto = request.files.get('foto')
        estado = request.form.getlist('estado')
        categoria = request.form.getlist('categoria')
        descricao = request.form.get('descricao')
        status = request.form.getlist('status')

        filename = None
        if foto and foto.filename != '':
            filename = secure_filename(foto.filename)
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        estado_str = ', '.join(estado)
        categoria_str = ', '.join(categoria)
        status_str = ', '.join(status)

        try:
            conn = conectar_mysql()
            cursor = conn.cursor()
            sql = '''
                INSERT INTO produtos (foto, estado, categoria, descricao, status)
                VALUES (%s, %s, %s, %s, %s)
            '''
            valores = (filename, estado_str, categoria_str, descricao, status_str)
            cursor.execute(sql, valores)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao inserir no banco: {e}")

        return redirect(url_for('index'))

    return render_template('cadastro_de_itens.html')

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