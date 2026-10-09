import os
os.system('cls')

vetor_notas = []

for i in range(3):
    nota = float(input('digite uma nota'))
    vetor_notas.append(nota) #inserindo a nota no vetor de notar

for i in range(3):
    print(f'Nota: {vetor_notas[i]}')