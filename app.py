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
    conn = get_db_conn()
    cursor = conn.cursor()
    interesses = conn.execute('SELECT * FROM interesse;').fetchall()
    inscricao_concluida = False
    form = FormularioCadastro()

    if form.validate_on_submit():
        nome = form.nome.data
        sobrenome = form.sobrenome.data
        idade = form.idade.data
        whatsapp = form.whatsapp.data
        semestre_atual = form.semestre_atual.data
        curso = form.curso.data
        sobre = form.sobre.data
        
        cursor.execute(
            'INSERT INTO aluno (nome, sobrenome, idade, whatsapp, semestre, curso_id, sobre) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (nome, sobrenome, idade, whatsapp, semestre_atual, curso, sobre)
        )
        conn.commit()
        conn.close()

        inscricao_concluida = True
    return render_template('inscricao.html', form=form, interesses=interesses, inscricao_concluida=inscricao_concluida)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    conn = get_db_conn()
    alunos = conn.execute('SELECT * FROM aluno;').fetchall()
    return render_template('admin.html', alunos=alunos)

@app.route('/manual', methods=['GET', 'POST'])
def manual():
    conn = get_db_conn()
    linhas = conn.execute('SELECT * FROM onibus;').fetchall()
    return render_template('manual-dos-bixos.html', linhas=linhas)

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
