class AuAu:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def Latir(self):
        print('Woff Woff')

Cachorro = AuAu('Totó',40)
Cachorro.Latir()
print('O cachorro',Cachorro.nome,'de',Cachorro.idade,'anos está latindo para você')
