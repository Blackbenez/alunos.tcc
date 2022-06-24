import sqlite3
import os.path
import os

nome_banco = "classe.db"

if os.path.exists(nome_banco): 
    os.unlink(nome_banco)
    
conexao = sqlite3.connect(nome_banco)
cursor = conexao.cursor() 
consulta = """CREATE TABLE Classe (
id INTEGER PRIMARY KEY AUTOINCREMENT,
aluno TEXT,
etnia TEXT,
idade INTEGER,
aprovados BOLEAN,
concluiram   BOLEAN,
sexo TEXT,
familiares  INT,
filhos INT
)
"""
cursor.execute(consulta) 
conexao.close() 