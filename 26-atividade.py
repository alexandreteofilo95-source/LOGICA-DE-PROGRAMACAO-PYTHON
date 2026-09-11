import os
os.system('cls')

# ENTRADA
nome = input('Qual seu nome: ')
sexo = input('Qual seu sexo F PARA FEMININO OU M PARA MASCULINO: ').upper()
altura = float(input('Digite sua altura: '))
peso_m = (72.7 * altura) - 58
peso_f = (62.1 * altura) - 44.7
match (sexo):
    case 'M' | "MASCULINO":
        print(f'Seu peso ideal é: {peso_m}')
    case 'F' | "FEMENINO":
        print(f'Seu peso ideal é: {peso_f}')
    case _:
        print('escolha o sexo feminino ou masculino')