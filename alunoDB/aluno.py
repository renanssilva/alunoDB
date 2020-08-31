import sqlite3

# definindo o diretóriode onde iremos criar o banco de dados
path = '/home/renan/sqlite/aluno'
print(path)

# atribuir uma conexão com o banco de dados
conn = sqlite3.connect(path+"/alunos.db")
print(conn)
print(type(conn))

cursor = conn.cursor()


def criar_tabela():
    cursor.execute('CREATE TABLE IF NOT EXISTS dados (id integer, unix real, keyword text, datestamp text, value real)')


criar_tabela()

1