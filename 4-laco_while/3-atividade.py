import os
os.system('cls')
soma = 0

for i in range(2):
    while True:
        numero = float(input(f'Digite sua {i+1}º nota: '))
        if numero >= 0 and numero <=10:
            soma = numero + numero
            break
        else:
            print('invalido, escolha um numero entre 1 e 10')

media = soma / 2
print(f'Sua media foi {media}')
        