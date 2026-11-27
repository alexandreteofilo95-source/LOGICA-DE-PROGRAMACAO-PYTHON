from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int
    endereco: str

QUANTIDADE_CLIENTE = 3

lista_cliente = []

for i in range(QUANTIDADE_CLIENTE):
    novo_cliente = Cliente(
        nome=input('Digite seu nome: '),
        email=input('Digite seu email: '),
        telefone=int(input('Digite seu telefone: ')),
        endereco=input('Digite seu endereço: ')
    )
    lista_cliente.append(novo_cliente)

    arquivo = 'dados_clientes.csv'
    with open (arquivo, 'a') as aquivo_clientes:
        for clientes in lista_cliente:
            aquivo_clientes.write(f'{clientes.nome}, {clientes.email}, {clientes.telefone}, {clientes.endereco}')
    print('clente salvo com sucesso!')