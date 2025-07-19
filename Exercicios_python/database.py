import sqlite3

conexao = sqlite3.connect("alunos.db")

cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS aluno(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               notas REAL NOT NULL
               )      """)

conexao.commit()

cursor.close()
conexao.close()

