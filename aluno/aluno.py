from aluno.notas import Notas


class Aluno:

    def __init__(self, nome, sobrenome, numero, serie, notas, participacao, faltas):
        self.codigo = None
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.numero: int = numero
        self.serie: int = serie
        self.notas: Notas = notas
        self.participacao: int = participacao
        self.faltas: int = faltas

    def __str__(self) -> str:
        return f'Aluno : {self.toDict()}'

    def toDict(self):
        """Devolve um Dicionário com as informações dos alunos"""
        pass

    def getNotas(self) -> list:
        """Método pega as notas dos alunos da classe Notas"""
        pass
