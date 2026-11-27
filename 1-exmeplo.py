from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Clientes:
    nome: str
    idade: int
    altura: float


QUANTIDADE_CLIENTES = 2

lista_clientes = []

for i in range(QUANTIDADE_CLIENTES):
    novo_cliente = Clientes(
        nome= input('Digite seu nome: '),
        idade= int(input('Digite sua idade: ')),
        altura= float(input('Digite sua altura: '))
    )
    lista_clientes.append(novo_cliente)

# Salvando em um arquivo.
    arquivo = 'dados_clientes.csv'
    with open (arquivo, 'a') as aquivo_clientes:
        for clientes in lista_clientes:
            aquivo_clientes.write(f'{clientes.nome}, {clientes.idade}, {clientes.altura}\n')

    print('clente salvo com sucesso!')