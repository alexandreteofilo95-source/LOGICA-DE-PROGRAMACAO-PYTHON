from dataclasses import dataclass
import os
os.system('cls')
@dataclass
class produto:
    nome: str
    preco: float



lista_produtos = []

def mostrar_dados(lista_produtos):
    for i in range(3):
        print(f'{i+1} - {lista_produtos[i]}')

print('= SOLICITANDO DADOS =')
for i in range(3):
    produto = input('digite o nome do produto: ')
    lista_produtos.append(produto)

print('\n= EXIBINDO DADOS =')
mostrar_dados(lista_produtos)
