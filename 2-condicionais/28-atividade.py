import os
os.system('cls')
# ENTRADA
nome = input('Qual seu nome: ')
sexo = input('qual seu sexo: ').upper()
estado_civil = input('qual seu estado civil: ').upper()
#PROCESSAMENTO

if sexo == 'FEMININO' and estado_civil == 'CASADO':
    resultado = int(input('Digite quanto tempo de casado: '))
    print(f'\nnome: {nome}')
    print(f'sexo: {sexo}')
    print(f'estado civil: {estado_civil}')
    print(f'anos de casado: {resultado}')
else:
    print(f'\nnome: {nome}')
    print(f'sexo: {sexo}')
    print(f'estado civil: {estado_civil}')

    
#SAIDA