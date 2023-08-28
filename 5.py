class Aluno:
    def __init__(self, nome, nota1,nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        media = (self.nota1 + self.nota2) / 2
        return media

Resultado = Aluno("kris",8,8)
print(f'A média do aluno {Resultado.nome} é {Resultado.media()}')