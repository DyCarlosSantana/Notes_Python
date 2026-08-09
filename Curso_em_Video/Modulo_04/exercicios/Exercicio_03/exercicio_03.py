from rich import print

class ContaBancaria:
    """
        Cria uma conta bancaria que permite fazer saques e depositos.
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
    
    def deposito(self, valor):
        self.saldo += valor
        print (f"Deposito de R${valor:.2f} autorizado")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print (f"Saque de R${valor:.2f} realizado")
        else:
            print (f"Saque de R${valor:.2f} não autorizado, [red]saldo insuficiente![/red]")

    def __str__(self):
        print (f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo")

c1 = ContaBancaria(112, "Edy Carlos", 3000)
c1.deposito(500)
c1.saque(5000)