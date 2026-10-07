import os
os.system('cls')
par = 0
impar = 0
inteiro = 0
while True:
    n = int(input('digite um numero inteiro: '))
    if n % 2 == 0:
        par +=1
        print(f'numeros pares: {par}')

    elif n % 2 == 0:
        impar +=1
        print(f'numeros impares: {impar}')
    else:
        n % 1 == 0
        inteiro +=1
        print(f'numeros inteiros: {inteiro}')

print('fim')