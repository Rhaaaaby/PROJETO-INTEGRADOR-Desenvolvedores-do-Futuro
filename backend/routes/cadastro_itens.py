from flask import request, redirect, url_for, render_template, current_app, Blueprint
from werkzeug.utils import secure_filename
import os
#import pymysql
import mysql.connector

cadastro_itens_bp = Blueprint('cadastro_itens', __name__)

def conectar_mysql():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        db='mydb'
        #charset='utf8mb4',
        #cursorclass=pymysql.cursors.DictCursor
    )

@cadastro_itens_bp.route('/cadastro_itens', methods=['GET', 'POST'])
def cadastro_itens():
    if request.method == 'POST':
        nome = request.form.get('nome')
        foto = request.files.get('foto')
        estado = request.form.get('estado')
        categoria = request.form.get('categoria_id')
        descricao = request.form.get('descricao')
        status = request.form.get('status')

        filename = None
        if foto and foto.filename != '':
            filename = secure_filename(foto.filename)
            foto.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        try:
            conn = conectar_mysql()
            cursor = conn.cursor()

            # Inserção no banco de dados
            cursor.execute('INSERT INTO Cadastro_Produto (Nome, Descricao) VALUES (%s, %s)', (nome, descricao))
            id_cadastro_produto = cursor.lastrowid

            # Inserção na tabela Produto
            sql = '''
                INSERT INTO Produto (Nome, Imagem_url, Estado, Categoria_id_Categoria, Descricao, Status, Usuario_id_Usuario, Cadastro_Produto_id_Cadastro_Produto, Criado_em)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW())
            '''

            imagem_url = f"uploads/{filename}" if filename else "images/default.png"

            valores = (
                nome,
                imagem_url,
                estado,
                categoria,
                descricao,
                status,
                2,
                id_cadastro_produto  # Aqui você pode usar o id do cadastro de produto
                # futuramente substituir os valores por números dinamicos
                # 1 e 2 são placeholders para Usuario_id_Usuario e Cadastro_Produto_id_Cadastro_Produto
            )
            cursor.execute(sql, valores)

            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao inserir no banco: {e}")

        return redirect(url_for('doacoes.doacoes'))  # vai pra página de doações

    return render_template('cadastro_de_itens.html')

from flask import send_from_directory

@cadastro_itens_bp.route('/uploads/<path:filename>')
def servir_uploads(filename):
    pasta_uploads = os.path.abspath(os.path.join(cadastro_itens_bp.root_path, '..', 'static', 'uploads'))
    return send_from_directory(pasta_uploads, filename)
