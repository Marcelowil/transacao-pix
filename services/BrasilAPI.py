import requests

# Endpoint da BrasilAPI para obter informações sobre bancos
url = "https://brasilapi.com.br/api/banks/v1"

response = requests.get(url)

if response.status_code == 200:
    bancos = response.json()
    for banco in bancos:
        # print(f"Nome: {banco['name']}, Código: {banco['code']}")
        # print(f"Código: {banco['code']}")
        pass
else:
    print("Falha ao obter os dados.")

def buscar_nome_banco(agencia):
    for banco in bancos:
        if agencia.zfill(4) in str(banco['code']).zfill(4):
            nome = banco['name']
    return nome    
            