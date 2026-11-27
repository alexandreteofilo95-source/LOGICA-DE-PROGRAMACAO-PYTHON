from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Clientes:
    nome: str
    email: str
    telefone: int
    endereco: str



lista_cliente = []


# Lendo um arquivo.
arquivo = 'dados_clientes.csv'
with open (arquivo, 'r') as aquivo_clientes:
    for linha in aquivo_clientes:
        nome,email,telefone,endereco = linha.strip().split(',')
        lista_cliente.append(Clientes(
            nome= nome,
            email= email,
            telefone= telefone,
            endereco=endereco
        ))

print('\nExibindo dados dos clientes: ')
for cliente in lista_cliente:
    print(f'nome: {cliente.nome}')
    print(f'email: {cliente.email}')
    print(f'telefone: {cliente.telefone}')
    print(f'endereço: {cliente.endereco}')
    print('===========================')