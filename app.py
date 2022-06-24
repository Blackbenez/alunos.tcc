import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS
from itsdangerous import base64_encode 

def pega_conexao():
    nome_banco ="classe.db"
    con = sqlite3.connect(nome_banco)
    return con  

app = Flask(__name__)
CORS(app)

@app.route("/")
def raiz():
    return "nosso trabalho de conclusão de curso!!"

@app.route("/todos")
def todos():
    con = pega_conexao()
    cur = con.cursor()
    #
    try:
        cur.execute("SELECT * FROM Classe")
    except:
        con.close()
        return jsonify("erro consulta")
    
    dados = cur.fetchall()
    con.close()
    return jsonify(dados)

@app.route("/lista/<int:id>")
def lista_um(id):
    con = pega_conexao()
    cur = con.cursor()
    try:
     cur.execute(f"SELECT * FROM classe WHERE ID={id}")
    except:
        con.close()
        return jsonify("Erro ao consular o banco")
    
    dados =  cur.fetchone()
    con.close()
    return jsonify(dados)
    
if __name__ == "__main__":
    app.run()
    