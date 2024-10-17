class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo #privada
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self): #o jeito certo é ter um método
        # ...
        return self._saldo

conta = Conta(100)
print(conta._saldo) #errado manipular dessa forma, porem vai funcionar
conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
