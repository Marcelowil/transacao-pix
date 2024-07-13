import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import cadastrar_chaves_db


def retornar_menu(cpf, agencia):
    from menu import acessar_menu
    acessar_menu(cpf, agencia)


chaves = """
Selecione o tipo de chave:
[1] - CPF
[2] - Email
[3] - Telefone
"""

def cadastrar_chave(usuario):

    while True:
        opcao = int(input(chaves))
        
        if opcao == 1:
           retorno = cadastrar_chaves_db("cpf", usuario.id_usuario)
        elif opcao == 2:
            retorno = cadastrar_chaves_db("email", usuario.id_usuario)
        elif opcao == 3:
            retorno = cadastrar_chaves_db("telefone", usuario.id_usuario)
        else:
            retorno = "Opção inválida, selecione novamente\n"

        print(retorno)
        retornar_menu(usuario.cpf, usuario.agencia)
        break
        