class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor
    
    def saldo(self):
        return f"{self._saldo:.2f}"
        
conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.saldo())