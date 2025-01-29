from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_db_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# def index():
    conn = get_db_conn()
    user = conn.execute('SELECT * FROM user').fetchall()
    conn.close()
    text = ''
    for u in user:
        text += u['email']
    return text

if __name__ == "__main__":
    app.run(debug=True)