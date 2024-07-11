import db
import criptografia
from menu import acessar_menu

while True:
    cpf = input("CPF: ")
    agencia = input("Agencia: ")
    senha = input("Senha: ")

    acesso = db.login(cpf, agencia)

    if criptografia.verificar_senha(senha, acesso[0]):
        acessar_menu(cpf, agencia)
        break
    else:
        print("CPF, agência ou senha inválidos!\n")

