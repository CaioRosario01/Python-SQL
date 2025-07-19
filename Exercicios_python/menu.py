
from main import Aluno


while True:
    print("Escolha uma das opções")
    print("[1] Adicionar Aluno")
    print("[2] Deletar Aluno")
    print("[3] Mostrar lista de alunos")
    print("[Sair] Para sair")


    escolha = (input(""))
    if escolha == ("Sair").lower():
        break
    if escolha == ("1"):
        Aluno1 = Aluno()
        Aluno1.adicionar_aluno()
    if escolha == ("2"):
        Aluno1 = Aluno()
        Aluno1.remover_aluno()
    if escolha ==("3"):
        Aluno1 = Aluno()
        Aluno1.mostrar_alunos()
