class Pessoas:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


Pessoa1 = Pessoas('Kris',16)
print('O nome e idade da primeira pessoa é:',Pessoa1.nome,'e',Pessoa1.idade)

Pessoa2 = Pessoas ('Yan', 18)
print('O nome e idade da segunda pessoa é:',Pessoa2.nome,'e',Pessoa2.idade)
