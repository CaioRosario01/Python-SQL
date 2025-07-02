
import pyodbc
import pandas as pd
from IPython.display import display

dados_conexao = ("Driver=SQLite3 ODBC Driver;"
                 "Server=localhost;"
                 "Database=chinook.db;"       
)                
conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM customers")
valores = cursor.fetchall()
descricao = cursor.description


colunas = [tupla[0] for tupla in descricao]
print(colunas)

tabela_clientes = pd.DataFrame.from_records(valores, columns = colunas)
display(tabela_clientes)


cursor.close()
conexao.close
