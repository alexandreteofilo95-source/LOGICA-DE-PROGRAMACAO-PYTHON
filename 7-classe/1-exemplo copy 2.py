from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #nome da variavel : tipo da variavel
    nome: str
    idade: int

lista_cliente = []




# SOLICITANDO DADOS DE DOIS CLIENTES
lista_cliente.append(Cliente('MARTA',30))
lista_cliente.append(Cliente('JOSE',40))

for cliente in lista_cliente:
    print(f'nome: {cliente.nome}')
    print(f'idade: {cliente.idade}')
    print('='*15)