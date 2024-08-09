import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import cadastrar_chaves_db, retornar_saldo, identificar_destinatario, login, transferencia
import criptografia
from formatar_chaves import mascarar_chave, mascarar_cpf, validar_chave_destinatario
from BrasilAPI import buscar_nome_banco

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

def realizar_transferencia(usuario):
    valor_transferencia = float(input("Digite o valor a ser transferido: "))

    if valor_transferencia < retornar_saldo(usuario.id_usuario):
            chave_destinatario = input("Para quem você deseja realizar a transferência?\nDigite a chave: ")
            chave_destinatario = validar_chave_destinatario(chave_destinatario)
            destinatario, tipo_chave = identificar_destinatario(chave_destinatario)
            
            confirmacao = input(confirmar_dados_transferencia(destinatario.nome, valor_transferencia, destinatario.cpf, destinatario.agencia, tipo_chave, destinatario.chave))
            
            while True:
                match confirmacao.upper():
                    case 'S':
                        confirmacao_senha = input('Digite sua senha: ')
                        if criptografia.verificar_senha(confirmacao_senha, login(usuario.cpf, usuario.agencia)[0]):
                            print(transferencia(usuario, destinatario, valor_transferencia))
                            retornar_menu(usuario.cpf, usuario.agencia)
                        else:
                            print("Senha inválida")
                        break
                    case 'N':
                        print("Transferencia cancelada")
                        break
                    case _:
                        print("Escolha inválida")
                        
    else:
        print("Valor selecionado ultrapassa seu saldo em conta.")
        retornar_menu(usuario.cpf, usuario.agencia)

def confirmar_dados_transferencia(nome, valor, cpf, agencia, tipo, chave):
    return f"""
Para: {nome} - Valor R$:{valor:.2f}
CPF: {mascarar_cpf(cpf)} - {buscar_nome_banco(agencia)}
Chave: {mascarar_chave(tipo, chave)}
Deseja confirmar a transferência (S/N)? 
"""

