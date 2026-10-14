import os
os.system('cls')

print('= INSERINDO NOMES NO VETOR =')

vetor_numeros = []
for i in range(5):
    nome = input('Digite um nome: ')
    vetor_numeros.append(nome)

print('\n= EXIBINDO NOMES DO VETOR =')
for  i in vetor_numeros:
    print(f'valor: {i}')