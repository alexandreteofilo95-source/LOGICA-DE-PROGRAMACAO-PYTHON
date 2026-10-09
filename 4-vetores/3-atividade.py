import os
os.system('cls')

vetor_nome = []

for i in range(4):
    nome = input(f'digite {i+1} nome: ')
    vetor_nome.append(nome) #inserindo a nota no vetor de notar

for i in range(4):
    print(f'\nNota: {vetor_nome[i]}')