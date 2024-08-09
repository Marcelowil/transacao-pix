import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import retornar_extrato
from domain.transacao import Transacao

def consultar_extrato(opcao, id):
    gerar_transacao(retornar_extrato(opcao, id))


def gerar_transacao(extrato):
    for row in extrato:
        transacao = Transacao(row[1], row[2], row[4], row[5], row[3], row[0])
        print(transacao)
