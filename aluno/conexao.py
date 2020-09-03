import sqlite3

# definindo o diretóriode onde iremos criar o banco de dados
path = '/home/renan/alunoDB'
print(path)

# atribuir uma conexão com o banco de dados
conn = sqlite3.connect(path + "/alunos.db")

# definindo um cursor
cursor = conn.cursor()


# criando uma tabela (Schema)
def criar_tabela():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS dados ('
        'Código INTEGER PRIMARY KEY AUTOINCREMENT,'
        'Nome str,'
        'Sobrenome str,'
        'Número int,'
        'Série int,'
        'Notas_1_trimestre list,'
        'Notas_2_trimestre list,'
        'Notas_3_trimestre list,'
        'Participação int,'
        'Faltas int)')


criar_tabela()
