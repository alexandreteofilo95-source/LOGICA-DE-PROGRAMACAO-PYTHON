from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Clientes:
    nome: str
    idade: int
    altura: float



lista_clientes = []


# Lendo um arquivo.
arquivo = 'dados_clientes.csv'
with open (arquivo, 'r') as aquivo_clientes:
    for linha in aquivo_clientes:
        nome,idade,altura = linha.strip().split(',')
        lista_clientes.append(Clientes(
            nome=nome,
            idade=int(idade),
            altura=float(altura)
            ))

print('\nExibindo dados dos clientes: ')
for cliente in lista_clientes:
    print(f'nome: {cliente.nome}')
    print(f'idade: {cliente.idade}')
    print(f'altura: {cliente.altura}')
    print('===========================')