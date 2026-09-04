import os 
os.system('cls')
# ENTRADA
usuario = input('usuario: ')
media = float(input('digite sua media: '))
falta = int(input('digite o seu numero de falta: '))

#PROCESSAMENTO
if media >= 7.0 and falta <= 40:
    print('aprovado')
else:
    print('reprovado')