
# 📚 Sistema de Cadastro de Alunos

Este é um projeto simples em Python com interface de linha de comando para cadastro, remoção e visualização de alunos com suas respectivas notas. Os dados são armazenados em um banco de dados SQLite.

## 🚀 Funcionalidades

- ✅ Cadastrar aluno com nome e nota
- ✅ Remover aluno pelo nome
- ✅ Listar todos os alunos e suas notas em formato de tabela
- ✅ Armazenamento persistente com SQLite
- ✅ Apresentação da lista de alunos com `pandas` para uma exibição organizada

## 🛠 Tecnologias Utilizadas

- Python 3.x
- SQLite3 (banco de dados local)
- Pandas (visualização de dados)

## 📂 Estrutura dos Arquivos

```
Exercicios_python/
│
├── alunos.db            # Banco de dados SQLite
├── database.py          # Criação da tabela no banco
├── main.py              # Classe principal Aluno com métodos de CRUD
├── menu.py              # Interface CLI com o menu interativo
└── __pycache__/         # Arquivos compilados automaticamente pelo Python
```

## 📌 Como Executar

1. **Clone ou baixe o repositório**

2. **Instale as dependências** (se ainda não tiver o pandas):
```bash
pip install pandas
```

3. **Crie o banco de dados** (executando o script `database.py` uma vez):
```bash
python database.py
```

4. **Execute o sistema principal**:
```bash
python menu.py
```

5. **Siga as instruções no menu**:
```
[1] Adicionar Aluno
[2] Deletar Aluno
[3] Mostrar lista de alunos
[Sair] Para sair
```

## 🧠 Exemplos

- Ao adicionar um aluno:
  - Nome: João
  - Nota: 8.5

- A listagem será exibida como:
```
   Nome  Nota
0  João   8.5
```

## 🔧 Futuras Melhorias (Sugestões)

- Implementar atualização de nota
- Validações de entrada (evitar nomes vazios ou notas inválidas)
- Interface gráfica com Tkinter ou Web (Flask/Django)
- Exportar lista de alunos em CSV ou Excel

## 👨‍💻 Autor

Caio Rosário  
Projeto educacional com fins de aprendizado em Python + SQLite + POO.
