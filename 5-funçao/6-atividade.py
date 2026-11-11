import os
os.system('cls')
def tabuada(numero):
    for i in range(1,10):
        print(f'{numero} * {i+1}= {numero * i}')

numero = int(input('digite um numero: '))

print('\n = exibindo dados =')
tabuada(numero)





