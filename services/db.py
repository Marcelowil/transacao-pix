import mysql.connector
from validate_docbr import CPF

config = {"host": "localhost", "user": "root", "password": "1234", "database": "db_pix"}
conexao = mysql.connector.connect(**config)
cursor = conexao.cursor()


def login(cpf, agencia):
    cpf = formatar_cpf(cpf)
    
    cursor.execute("SELECT senha FROM tb_usuarios WHERE agencia LIKE %s AND cpf = %s;", ("%" + agencia, cpf, ))
    acesso = cursor.fetchone()
    return acesso

def buscar_usuario(cpf, agencia):
    cpf = formatar_cpf(cpf)
    
    cursor.execute("SELECT * FROM tb_usuarios WHERE cpf = %s AND agencia LIKE %s;" (cpf, "%" + agencia,))
    usuario = cursor.fetchone()
    return usuario

def formatar_cpf(cpf):
    cpf = CPF().mask(cpf)
    return cpf
