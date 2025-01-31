import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from forms import FormularioCadastro

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = FormularioCadastro()
    if form.validate_on_submit():
        # Aqui você pode processar os dados do formulário
        nome = form.nome.data
        sobrenome = form.sobrenome.data
        idade = form.idade.data
        curso = form.curso.data
        whatsapp = form.whatsapp.data
        semestre_atual = form.semestre_atual.data
        # Fazer algo com os dados
        return 'Cadastro realizado com sucesso!'
    return render_template('form.html', form=form)

def get_db_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# # def index():
#     conn = get_db_conn()
#     user = conn.execute('SELECT * FROM user').fetchall()
#     conn.close()
#     text = ''
#     for u in user:
#         text += u['email']
#     return text


if __name__ == "__main__":
    app.run(debug=True)