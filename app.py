import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, make_response, jsonify
from werkzeug.exceptions import abort
from forms import FormularioCadastro
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'y#VGtGr9.SZ#8?1RMlk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:H%40XRTei%24K5aPGU.@db.otehdyoibzmgrqufxbgm.supabase.co:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    temas = conn.execute('SELECT * FROM tema;').fetchall()
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
        temas = request.args.getlist('tema')
        
        cursor.execute(
            'INSERT INTO aluno (nome, sobrenome, idade, whatsapp, semestre, curso_id, sobre) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (nome, sobrenome, idade, whatsapp, semestre_atual, curso, sobre)
        )
        aluno_id = cursor.lastrowid

        conn.commit()
        conn.close()

        inscricao_concluida = True

    response = make_response(render_template('inscricao.html', form=form, temas=temas, inscricao_concluida=inscricao_concluida))
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    conn = sqlite3.connect('database.db')
    alunos = conn.execute('SELECT * FROM aluno;').fetchall()
    return render_template('admin.html', alunos=alunos)

# def get_db_conn():
#     conn.row_factory = sqlite3.Row
#     return conn

# Definindo os Modelos de Dados
class Aluno(db.Model):
    __tablename__ = 'aluno'  # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    sobrenome = db.Column(db.String(255), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    whatsapp = db.Column(db.String(20), nullable=False)
    semestre = db.Column(db.SmallInteger)
    sobre = db.Column(db.Text)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    
    curso = db.relationship('Curso', backref='alunos')  # Relacionamento com a tabela 'curso'

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key=True)
    sigla = db.Column(db.String(10), nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    turno = db.Column(db.String(10), nullable=False)

# Endpoint para retornar todos os alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()  # Obtém todos os alunos
    alunos_list = []
    for aluno in alunos:
        alunos_list.append({
            'id': aluno.id,
            'nome': aluno.nome,
            'sobrenome': aluno.sobrenome,
            'idade': aluno.idade,
            'whatsapp': aluno.whatsapp,
            'semestre': aluno.semestre,
            'sobre': aluno.sobre,
            'curso': aluno.curso.nome
        })
    return render_template('admin.html', alunos=alunos)

if __name__ == '__main__':
    app.run(debug=True)

import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")


if __name__ == "__main__":
    app.run(debug=True)