import os
os.system('cls')

# ENTRADA
nota = float(input('digite uma nota: '))
# PROCESAMENTO
if nota >= 0 and nota <=10:
    print(f'sua nota é: {nota}')
else:
    print('A nota deve ser de 0 a 10')