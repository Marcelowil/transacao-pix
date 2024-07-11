import mysql.connector
import sys
import os
from validate_docbr import CPF
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from domain.usuario import Usuario



config = {"host": "localhost", "user": "root", "password": "1234", "database": "db_pix"}
conexao = mysql.connector.connect(**config)
cursor = conexao.cursor()


def login(cpf, agencia):
    cpf = formatar_cpf(cpf)
    
    cursor.execute("SELECT senha FROM tb_usuarios WHERE agencia LIKE %s AND cpf = %s;", ("%" + agencia, cpf, ))
    acesso = cursor.fetchone()
    return acesso

def buscar_usuario_chave(cpf, agencia):
    cpf = formatar_cpf(cpf)
    
    cursor.execute("SELECT * FROM tb_usuarios WHERE cpf = %s AND agencia LIKE %s;", (cpf, "%" + agencia,))
    usuario = cursor.fetchone()

    cursor.execute("SELECT tipo, valor FROM tb_chaves_pix WHERE usuario_id = %s;", (usuario[0],))
    chaves = cursor.fetchall()

    lista_chaves={}
    for row in chaves:
        lista_chaves[row[0]] = row[1]

    usuario = Usuario(usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6], usuario[7], lista_chaves, usuario[0])
    return usuario

def formatar_cpf(cpf):
    cpf = CPF().mask(cpf)
    return cpf
