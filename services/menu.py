import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from domain.usuario import Usuario
from services.db import buscar_usuario_chave


menu = """
[1] - Consultar Saldo
[2] - Extrato
[3] - Pix
[0] - Sair

"""
def acessar_menu(cpf, agencia):
    usuario = buscar_usuario_chave(cpf, agencia)
    print(usuario.nome)

    while True:
        opcao = int(input(menu))

        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 0:
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação digitada")