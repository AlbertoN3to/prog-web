class conta:

    def __init__(self, saldo, numero_da_conta):
        self.saldo = saldo
        self.numero_da_conta = numero_da_conta


    def creditar(self,x):
        self.saldo += x
        return print("\nNovo saldo = "+str(self.saldo)+"\n")


    def debitar(self,x):
        self.saldo -= x
        return print("\nNovo saldo = "+str(self.saldo)+"\n")


    def exibir(self):
        return print("\nNúmero da conta ="+self.numero_da_conta+"\nSaldo ="+str(self.saldo)+"\n")


    def __del__(self):
        print("\nConta deletada")
        pass