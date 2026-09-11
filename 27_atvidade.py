import os
os.system('cls')
# ENTRADA
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

soma = a + b
# PROCESSAMNETO
if soma < c:
    print(f'{a} + {b} é menor que {c}')
elif soma > c:
    print(f'{a} + {b} maior que {c}')
else:
    print('valor invalido')
# SAIDA