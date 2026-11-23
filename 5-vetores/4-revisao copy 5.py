import os
os.system('cls')

print('= INSERINDO 5 LIVROS NO VETOR =')

vetor_numeros = []
for i in range(5):
    livro = input(f'Digite {i+1}º LIVRO: ')
    vetor_numeros.append(livro)

print('\n= EXIBINDO livros DO VETOR =')
for indice, i in enumerate(vetor_numeros, start=1):
    print(f'{indice}º: {i}')