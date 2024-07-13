import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.db import buscar_usuario_chave, retornar_saldo
from services.BrasilAPI import buscar_nome_banco
from services.pix import cadastrar_chave

menu = """
[1] - Consultar Saldo
[2] - Extrato
[3] - Pix
[0] - Sair

"""

menu_pix = """
[1] - Realizar Transferência
[2] - Cadastrar Chave
"""
def acessar_menu(cpf, agencia):
    cpf = cpf.replace('.', '').replace('-', '')
    usuario = buscar_usuario_chave(cpf, agencia)
    cabecalho = f"{usuario.nome} - Banco: {buscar_nome_banco(usuario.agencia)} | Conta: {usuario.conta}"
    print(f"\nBem-vindo {cabecalho}")

    while True:
        opcao = int(input(menu))

        if opcao == 1:
            print(cabecalho + "\n" + retornar_saldo(usuario.id_usuario))
        elif opcao == 2:
            pass
        elif opcao == 3:
            opcao_pix = int(input(menu_pix))

            if opcao_pix == 1:
                pass
            elif opcao_pix == 2:
                cadastrar_chave(usuario)
            else:
                print("Operação inválida, por favor selecione novamente a operação digitada")
        elif opcao == 0:
            sys.exit()
        else:
            print("Operação inválida, por favor selecione novamente a operação digitada")