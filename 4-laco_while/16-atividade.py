import os
os.system('cls')
par = 0
impar = 0
inteiro = 0
quantidades_par = 0
soma = 0
while True:
    n = int(input('digite um numero inteiro: '))
    if n % 2 == 0:
        par +=1
        quantidades_par += 1
        soma +=par
        media = quantidades_par / soma

    else:
        impar +=1
    if n == 0:
        print(f'\numeros pares: {par}')
        print(f'media de pares: {media}')
        print(f'numeros impares: {impar}')
        print(f'numeros inteiros: {n}')
        print('fim')
