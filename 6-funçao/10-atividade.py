import os
os.system('cls')

def calcular_notas(lista_notas):
    return sum(lista_notas) / len(lista_notas)
def mostra_resultado(media,lista_notas):
    print('\n= EXIBINDO DADOS =')
    for nota in lista_notas:
        print(f'nota: {nota}')

    print(f'\nMedia: {media}')

lista_notas = []

for i in range(3):
    nota = float(input('digite sua nota: '))
    lista_notas.append(nota)

media = calcular_notas(lista_notas)
mostra_resultado(media,lista_notas)