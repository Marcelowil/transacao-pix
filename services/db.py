import mysql.connector
import sys
import os
from validate_docbr import CPF
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from domain.usuario import Usuario
from services.BrasilAPI import buscar_nome_banco



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

def retornar_saldo(id):
    cursor.execute("SELECT saldo FROM tb_usuarios WHERE id = %s;", (id, ))
    saldo = cursor.fetchone()

    return f"Saldo: R${saldo[0]:.2f}"

def cadastrar_chaves_db(tipo, id):
    cursor.execute("SELECT * FROM tb_usuarios WHERE id = %s;", (id,))
    usuario = cursor.fetchone()
    
    try:
        if tipo == 'cpf':
            valor = usuario[2]
        elif tipo == 'telefone':
            valor = usuario[3]
        else:
            valor = usuario[4]

        cursor.execute("INSERT INTO tb_chaves_pix(usuario_id, tipo, valor) VALUES (%s, %s, %s);", (id, tipo, valor, ))
        conexao.commit()
        return f"{tipo.upper()}: {valor} cadastrado como chave pix no Banco {buscar_nome_banco(usuario[5])}"
    except Exception:
        conexao.rollback()
        return f"{valor} já cadastrado como chave pix!"


def formatar_cpf(cpf):
    cpf = CPF().mask(cpf)
    return cpf
