from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #nome da variavel : tipo da variavel
    nome: str
    idade: int
    altura: float
    peso: float

lista_cliente = []




# SOLICITANDO DADOS DE DOIS CLIENTES
for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('digite seu nome: '),
        idade = int(input('digite sua idade: ')),
        altura = float(input('qual sua altura: ')),
        peso = float(input('qual seu peso: '))
    )
    lista_cliente.append(dados_do_cliente)

print('\nEXIBINDO DADOS')
for cliente in lista_cliente:
    print(f'nome: {cliente.nome}')
    print(f'idade: {cliente.idade}')
    print(f'altura: {cliente.altura}')
    print(f'peso: {cliente.peso}')
    print('='*15)