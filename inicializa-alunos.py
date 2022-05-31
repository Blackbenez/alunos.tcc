nome_banco = "classe"

if os.path.exists(nome_banco): 

 conexao = sqlite3.connect(nome_banco)
 cursor = conexao.cursor() 
 consulta = """CREATE TABLE Alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno TEXT,
    etnia TEXT,
    idade INTEGER,
    aprovados BOLEAN,
    concluiram   BOLEAN,
    sexo TEXT,,
    familiares  INT,
    filhos INT
    """
cursor.execute(consulta) 


conexao.close() 