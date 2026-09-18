import os
os.system('cls')

print('= TABUADA =')
numero = int(input('Digite um numero: '))

for i in range(1,10):
    print(f'{numero} + {i} = {numero + i} ')

for i in range(1,10):
    print(f'{numero} - {i} = {numero - i} ')

for i in range(1,10):
    print(f'{numero} x {i} = {numero * i} ')
    
for i in range(1,10):
    print(f'{numero} / {i} = {numero / i} ')