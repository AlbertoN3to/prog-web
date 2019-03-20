#! /usr/bin/python3
from conta import conta

def criarConta ():
    print("Digite o saldo inicial.")
    x = int(input())
    print("Digite o número da conta.")
    y = input()
    return conta(x, y)

c1 = criarConta()

b = True

while b:
    print("Que operação desejas fazer?\nCreditar = 1\nDebitar = 2\nDados da Conta = 3\nDeletar a conta e criar uma nova = 4\nPressione qualquer outra tecla para sair.")
    user_input = input()

    if user_input == "1":
        print("Quanto desejas creditar?")
        c1.creditar(int(input()))
    elif user_input == "2":
        print("Quanto desejas debitar?")
        c1.debitar(int(input()))
    elif user_input == "3":
        c1.exibir()
    elif user_input == "4":
        c1.__del__()
        c1 = criarConta()
    else:
        break


# def media(x,y):
#     return print((x+y)/2)


# print("Digite o primeiro número.")
# x = int(input())
# print("Digite o segundo número.")
# y = int(input())

# media(x,y)
