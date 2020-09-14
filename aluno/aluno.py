import sqlite3


class Aluno:

    def __init__(self, nome, sobrenome, numero, serie, nota_1, nota_2, nota_3, participacao, faltas):
        # def __init__(self, codigo, nome, sobrenome):
        self.codigo = None
        self.nome = nome
        self.sobrenome = sobrenome
        self.numero = numero
        self.serie = serie
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
        self.participacao = participacao
        self.faltas = faltas

    def toDict(self):
        alunoDict = {
            "Código": self.codigo,
            'Nome': self.nome,
            'Sobrenome': self.sobrenome,
            'Número': self.numero,
            'Série': self.serie,
            'Nota 1': self.nota_1,
            'Nota 2': self.nota_2,
            'Nota 3': self.nota_3,
            'Participação': self.participacao,
            'Faltas': self.faltas
        }
        return alunoDict

    def __str__(self):
        return f'Aluno: {self.toDict()}'


class Banco:

    @staticmethod
    def addAluno(aluno):

        # atribuir uma conexão com o banco de dados
        conn = sqlite3.connect("/home/renan/alunoDB/alunos.db")

        #  definindo um cursor
        cursor = conn.cursor()

        # Adicionando Aluno
        inserir_aluno = f"""INSERT INTO dados 
        (Nome, Sobrenome, Número, Série, Notas_1_trimestre, Notas_2_trimestre, Notas_3_trimestre,Participação, Faltas)
        VALUES(
        "{aluno.nome}", "{aluno.sobrenome}", {aluno.numero}, {aluno.serie},
         {aluno.nota_1}, {aluno.nota_2}, {aluno.nota_3}, {aluno.participacao}, {aluno.faltas})"""

        # Executa o comando de inserir aluno:
        conn.execute(inserir_aluno)

        # Efetua um commit no banco de dados.Ñ é efetuado commit automaticamente.
        # Devemos commitar para salvar suas alterações.
        conn.commit()

    @staticmethod
    def removeAluno(code):
        # atribuir uma conexão com o banco de dados
        conn = sqlite3.connect("/home/renan/alunoDB/alunos.db")

        # definindo um cursor
        cursor = conn.cursor()

        # Executa o comando de deletar aluno:
        conn.execute(f'DELETE FROM dados WHERE Código = {code}')

        # Efetua um commit no banco de dados.Ñ é efetuado commit automaticamente.
        # Devemos commitar para salvar suas alterações.
        conn.commit()

    @staticmethod
    def listaAlunos():
        # atribuir uma conexão com o banco de dados
        conn = sqlite3.connect("/home/renan/alunoDB/alunos.db")

        # definindo um cursor
        cursor = conn.cursor()

        # Executa o comando de deletar aluno:
        lista = conn.execute('SELECT * FROM dados')
        for item in lista.fetchall():
            print(item)

        # Efetua um commit no banco de dados.Ñ é efetuado commit automaticamente.
        # Devemos commitar para salvar suas alterações.
        conn.commit()

    @staticmethod
    def buscaAluno(codigo):
        # atribuir uma conexão com o banco de dados
        conn = sqlite3.connect("/home/renan/alunoDB/alunos.db")

        # definindo um cursor
        cursor = conn.cursor()

        # Executa o comando de deletar aluno:
        lista = conn.execute(f'SELECT * FROM dados WHERE "Código" = "{codigo}"')
        print(lista.fetchall())

        # Efetua um commit no banco de dados.Ñ é efetuado commit automaticamente.
        # Devemos commitar para salvar suas alterações.
        conn.commit()


def menu():
    print("*******************************************\n"
          "1 - Adicionar Aluno:\n"
          "2 - Remover Aluno:\n"
          "3 - Listar Alunos:\n"
          "4 - Buscar Aluno:\n"
          "s - Sair do Programa\n"
          "*******************************************")


while True:
    menu()
    opcao = input('Escolha uma opção: ')
    if opcao not in ['1', '2', '3', '4', 's']:
        print('Opção inválida')
        continue

    if opcao == 's':
        break

    if opcao == '1':
        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        numero = int(input("Numero: "))
        serie = int(input("Série: "))
        nota_1 = input("Nota 1: ")
        nota_2 = input("Nota 2: ")
        nota_3 = input("Nota 3: ")
        participacao = int(input("Participação: "))
        faltas = int(input("Faltas: "))

        aluna = Aluno(nome, sobrenome, numero, serie, nota_1, nota_2, nota_3, participacao, faltas)

        Banco.addAluno(aluna)

        print(f"Alune {nome} {sobrenome} foi cadastrado com sucesso.")

    if opcao == '2':
        codigo = int(input('Digite o Código do aluno a ser removido: '))
        Banco.removeAluno(codigo)

    if opcao == '3':
        Banco.listaAlunos()

    if opcao == '4':
        nome = input('Digite o Nome do aluno a ser encontrado: ')
        Banco.buscaAluno(nome)
