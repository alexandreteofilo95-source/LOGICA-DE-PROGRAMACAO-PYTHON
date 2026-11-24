from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class paciente:
    nome: str
    idade: int
    telefone: int
    endereco: str

    def pacientes(self):
        print(f'nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'telefone: {self.telefone}')
        print(f'endereço: {self.endereco}')

    def dados(self):
        print(f'nome: {self.nome}')
        print(f'telefone: {self.telefone}')

    def outros_dados(self):
        print(f'nome: {self.nome}')
        print(f'telefone: {self.telefone}')

lista_dados = []

for i in range(1):
    dados_do_cliente = paciente(
    nome= input('digite seu nome: '),
    idade= int(input('digite sua idade: ')),
    telefone= input('digite seu telefone: '),
    endereco= input('digite seu endereço: ')
    )
    lista_dados.append(dados_do_cliente)

print('\n= EXIBINDO DADOS=')
for paciente in lista_dados:
    paciente.pacientes()

        

print('\n= EXIBINDO DADOS=')
for paciente in lista_dados:
    paciente.dados()

print('\n= EXIBINDO DADOS=')
for paciente in lista_dados:
    paciente.outros_dados()
