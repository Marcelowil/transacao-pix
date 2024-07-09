import mysql.connector

config = {
    'host': 'localhost', 
    'user': 'root', 
    'password': "1234",
    'database': 'db_pix'
}
conexao = mysql.connector.connect(**config)

cursor = conexao.cursor()