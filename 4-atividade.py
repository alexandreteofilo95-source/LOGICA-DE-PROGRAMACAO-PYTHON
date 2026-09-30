import os
os.system('cls')
soma = 0

for i in range(2):
    while True:
        numero = float(input(f'Digite sua {i+1}º nota: '))
        if numero < 0 or numero >10:
            print('invalido, escolha um numero entre 1 e 10')
        else:
            soma = numero + numero
            break
        

media = soma / 2
print(f'Sua media foi {media}')