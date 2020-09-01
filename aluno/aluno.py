class Aluno:

    def __init__(self, codigo, nome, sobrenome, numero, serie, nota_1, nota_2, nota_3, participacao, faltas):
        self.codigo = codigo
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
        return {"Código": self.codigo, 'Nome': self.nome, 'Sobrenome': self.sobrenome, 'Número': self.numero,
                'Série': self.serie, 'Nota 1': self.nota_1, 'Nota 2': self.nota_2, 'Nota 3': self.nota_3,
                'Participação': self.participacao, 'Faltas': self.faltas}
