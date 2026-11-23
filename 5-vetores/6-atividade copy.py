import os
os.system('cls')
NUMEROS_REPETICOES = 4
print('= ENSIRINDO NOTAS =')
numeros_vetores = []

for i in range(NUMEROS_REPETICOES):
    nota = float(input(f'Digite {i+1}º nota: '))
    numeros_vetores.append(nota)
    
    
    media = sum(numeros_vetores) / NUMEROS_REPETICOES
    maior = max(numeros_vetores)
    menor = min(numeros_vetores)

print('\n= EXIBINDO NOTAS E MEDIA =')
for indece, i in enumerate(numeros_vetores, start=1):
    print(f'{indece}º nota: {i}')

if media >= 7 and media <=10:
    print('\nAprovado')
    print(f'Sua media: {media}')
elif media >=5:
    print('\nrecuperação')
    print(f'Sua media: {media}')
else:
    print('\nReprovado')
    print(f'Sua media: {media}')

print('\n= EXIBINDO MAIOR E MENOR NOTAS DO VETOR =')
print(f'maior nota: {maior}')
print(f'menor nota: {menor}')

