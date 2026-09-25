import os
os.system('cls')
NUMEROS_REPETICOES = 3
n = 0
for i in range(NUMEROS_REPETICOES):
    n += int(input('digite sua nota: '))

    media = n / NUMEROS_REPETICOES
if media >= 7:
        print(f'Sua media foi: {media}')
        print('APROVADO')
elif media > 4:
        print(f'Sua media foi: {media}')
        print('RECUPERAÇAO')
else:
        print(f'Sua media foi: {media}')
        print('REPROVADO')
