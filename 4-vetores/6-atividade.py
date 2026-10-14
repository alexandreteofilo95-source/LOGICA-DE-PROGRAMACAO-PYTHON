import os
os.system('cls')
NUMEROS_REPETICOES = 3
print('= ENSIRINDO NOTAS =')
numeros_vetores = []

for i in range(NUMEROS_REPETICOES):
    nota = float(input(f'Digite {i+1}º nota: '))
    numeros_vetores.append(nota)
    soma = sum(numeros_vetores)
    media = soma / NUMEROS_REPETICOES

print('\n= EXIBINDO NOTAS E MEDIA =')
for indece, i in enumerate(numeros_vetores, start=1):
    print(f'{indece}º nota: {i}')
print(f'Sua media: {media}')