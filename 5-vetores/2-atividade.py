import os
os.system('cls')
soma = 0
vetores_nota = []
for i in range(2):
    nota = int(input('digite sua nota: '))
    soma +=nota
    media = soma / 2
    vetores_nota.append(media)
print(f'media: {vetores_nota[i]} ')