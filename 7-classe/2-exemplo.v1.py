from dataclasses import dataclass
import os
os.system('cls')

lista_clientes = []
@dataclass
class Cliente:
    nome: str
    telefone: int
    email: str 

#FUNÇÃO DENTRO DA CLASSE
    def mostra_dados(self):
        print(f'\nnome: {self.nome}')
        print(f'telefone: {self.telefone}')
        print(f'email: {self.email}')
        print('='*15)

print('= SOLICITANDO DADOS =')
for i in range(2):
    dados = Cliente(
    nome = input('digite seu nome: '),
    telefone= int(input('digite seu telefone: ')),
    email= input('digite seu email: ')
    )
    lista_clientes.append(dados)

for cliente in lista_clientes:
    cliente.mostra_dados()
