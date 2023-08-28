class ContaBancaria:
    def __init__(self,titular,saldo,numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def sacar(self, saque):
        self.saldo = self.saldo - saque

    def deposito(self, depositar):
        self.saldo = self.saldo + depositar

    def exibir(self):
        print(f'O saldo atual é: {self.saldo}')


Dindin = ContaBancaria('Kristhyan',1000,'1212')
Dindin.sacar(200)
Dindin.exibir()
Dindin.deposito(500)
Dindin.exibir()

