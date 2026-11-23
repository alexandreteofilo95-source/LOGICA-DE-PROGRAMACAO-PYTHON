import os
os.system('cls')
REPETICOES = 4
soma = 0
for i in range(REPETICOES):
    numeros = int(input('Digite um numero inteiro positivo: '))
    if numeros > 0:
        soma +=numeros
        media = soma / REPETICOES
        print(f'Sua media é: {media} ')
    else:
        print('FIM')
