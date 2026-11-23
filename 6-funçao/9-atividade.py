import os
from datetime import date
os.system('cls')

def nascimento(data):
    ano_atual = date.today().year
    resultado = ano_atual - data
    return resultado

data = int(input('digite o ano do seu nascimento: '))

print('\n= EXIBINDO DADOS =')
idade = nascimento(data)
print(f'Ano do nascimento: {data}')
print(f'Sua idade: {idade}')
