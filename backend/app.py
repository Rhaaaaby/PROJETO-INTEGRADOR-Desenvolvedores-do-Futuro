from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from werkzeug.utils import secure_filename

app = Flask(
    __name__,
    template_folder='../frontend',
    static_folder='../static'
)
app.secret_key = '12345'

UPLOAD_FOLDER = os.path.join(app.root_path, '../static/uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

        # Exibir dados no terminal (pode trocar por banco de dados)
        print({
            "foto": filename,
            "estado": estado,
            "categoria": categoria,
            "descricao": descricao,
            "status": status
        })
        return redirect(url_for('index'))

    return render_template('cadastro_de_itens.html')

if __name__ == '__main__':
    app.run(debug=True)
