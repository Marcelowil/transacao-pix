import requests

# Endpoint da BrasilAPI para obter informações sobre bancos
url = "https://brasilapi.com.br/api/banks/v1"

response = requests.get(url)

if response.status_code == 200:
    bancos = response.json()
    for banco in bancos:
        print(f"Nome: {banco['name']}, Código: {banco['code']}")
else:
    print("Falha ao obter os dados.")
