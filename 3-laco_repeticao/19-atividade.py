import os
os.system('cls')
NUMERO_REPETICOES = 4
n = 0
for i in range(NUMERO_REPETICOES):
    n += float(input(f'Digite sua {i+1}º nota:'))
    media = n / NUMERO_REPETICOES
print(f'sua media é {media}')