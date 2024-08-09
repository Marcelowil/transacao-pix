import mysql.connector
import sys
import os
import uuid
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.formatar_chaves import formatar_chaves
from domain.usuario import Usuario
from services.BrasilAPI import buscar_nome_banco


config = {"host": "localhost", "user": "root", "password": "1234", "database": "db_pix"}
conexao = mysql.connector.connect(**config)
cursor = conexao.cursor()


def login(cpf, agencia):    
    cursor.execute("SELECT senha FROM tb_usuarios WHERE agencia LIKE %s AND cpf = %s;", ("%" + agencia, cpf, ))
    acesso = cursor.fetchone()
    return acesso

def buscar_usuario_chave(cpf, agencia):    
    cursor.execute("SELECT * FROM tb_usuarios WHERE cpf = %s AND agencia LIKE %s;", (cpf, "%" + agencia,))
    usuario = cursor.fetchone()

    cursor.execute("SELECT tipo, valor FROM tb_chaves_pix WHERE usuario_id = %s;", (usuario[0],))
    chaves = cursor.fetchall()

    return gerar_usuario(usuario, chaves)
   

def retornar_saldo(id):
    conexao = mysql.connector.connect(**config)
    cursor = conexao.cursor()

    cursor.execute("SELECT saldo FROM tb_usuarios WHERE id = %s;", (id, ))
    saldo = cursor.fetchone()
    
    return saldo[0]

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
        valor = formatar_chaves(tipo, valor)
        return f"{tipo.upper()}: {valor} cadastrado como chave pix no Banco {buscar_nome_banco(usuario[5])}"
    except Exception:
        conexao.rollback()
        valor = formatar_chaves(tipo, valor)
        return f"{valor} já cadastrado como chave pix!"
    
def identificar_destinatario(valor):
    cursor.execute("SELECT u.cpf, u.agencia, p.tipo FROM tb_usuarios u LEFT JOIN tb_chaves_pix p ON u.id = p.usuario_id WHERE p.valor = %s;", (valor, ))
    destinatario = cursor.fetchone();
    return buscar_usuario_chave(destinatario[0], destinatario[1]), destinatario[2]

def transferencia(usuario, destinatario, valor):
    try:
        cursor.execute("UPDATE tb_usuarios SET saldo = saldo - %s WHERE id = %s;", (valor, usuario.id_usuario, ))
        cursor.execute("UPDATE tb_usuarios SET saldo = saldo + %s WHERE id = %s;", (valor, destinatario.id_usuario, ))
        cursor.execute("INSERT INTO tb_transacoes(id, valor, data_transacao, usuario_origem, usuario_destino, status_transacao) VALUES (%s, %s, %s, %s, %s, %s);", (str(uuid.uuid4()), valor, datetime.now(), usuario.id_usuario, destinatario.id_usuario, "Transferência confirmada",))
        conexao.commit()
        return "Transferência realizada"
    except Exception:
        conexao.rollback()
        cursor.execute("INSERT INTO tb_transacoes(id, valor, data_transacao, usuario_origem, usuario_destino, status_transacao) VALUES (%s, %s, %s, %s, %s, %s);", (str(uuid.uuid4()), valor, datetime.now(), usuario.id_usuario, destinatario.id_usuario, "Transferência não realizada",))
        return "Erro ao realizar a transferência"


def gerar_usuario(usuario, chaves):
    lista_chaves={}
    for row in chaves:
        lista_chaves[row[0]] = row[1]

    usuario = Usuario(usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6], usuario[7], lista_chaves, usuario[0])
    return usuario