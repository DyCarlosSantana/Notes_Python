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
        return (f"Deposito de R${valor:.2f} autorizado")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return (f"Saque de R${valor:.2f} realizado")
        else:
            return (f"Saque de R${valor:.2f} não autorizado, saldo insuficiente!")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo"

c1 = ContaBancaria(112, "Edy Carlos", 3000)
c1.deposito(500)
c1.saque(1500)
print(c1)