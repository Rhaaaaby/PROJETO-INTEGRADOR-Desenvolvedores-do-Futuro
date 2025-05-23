from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import mysql.connector

# Configuração do Flask
app = Flask(
    __name__,
    template_folder='../frontend',   # ajuste se necessário
    static_folder='../static'
)

# Pasta de uploads
UPLOAD_FOLDER = os.path.join(app.root_path, '../static/uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Função para conectar ao banco MySQL
def conectar_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",            
        password="admin",   
        database="doa"         
    )

# Rota principal do formulário
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 1. Coletar dados do formulário
        foto = request.files.get('foto')
        estado = request.form.getlist('estado')
        categoria = request.form.getlist('categoria')
        descricao = request.form.get('descricao')
        status = request.form.getlist('status')

        # 2. Salvar imagem
        filename = None
        if foto and foto.filename != '':
            filename = secure_filename(foto.filename)
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # 3. Converter listas em strings
        estado_str = ', '.join(estado)
        categoria_str = ', '.join(categoria)
        status_str = ', '.join(status)

        # 4. Inserir no banco de dados
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

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
