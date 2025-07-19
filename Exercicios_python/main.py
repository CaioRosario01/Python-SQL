
import sqlite3
import pandas as pd


class Aluno():
    def __init__(self):
        self

    def conectar_db(self):
        return sqlite3.connect('alunos.db')
        

    def adicionar_aluno(self):
        conexao = self.conectar_db()
        cursor = conexao.cursor()

        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))

        cursor.execute("INSERT INTO aluno(nome,notas) VALUES (?, ?)", (nome, nota))

        conexao.commit()
        conexao.close()

    def remover_aluno(self):
        conexao = self.conectar_db()
        cursor = conexao.cursor()

        deletar_Nome = input("Digite o nome do aluno para deletar: ")
        cursor.execute("DELETE FROM aluno WHERE nome = ?",(deletar_Nome,))

        conexao.commit()
        conexao.close()


    def mostrar_alunos(self):
        conexao = self.conectar_db()
        cursor = conexao.cursor()

        cursor.execute("SELECT nome, notas FROM aluno")
        dados = cursor.fetchall()
        
        df = pd.DataFrame(dados, columns=["Nome", "Nota"])
        print(df)

        conexao.commit()
        conexao.close()
