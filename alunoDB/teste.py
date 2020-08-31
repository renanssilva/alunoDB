class Aluno:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def mostra(self):
        return self.__nome


quem = Aluno('Renan')

print(quem.mostra)