from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #nome da variavel : tipo da variavel
    nome: str
    idade: int




# SOLICITANDO DADOS EM UM CLIENTE.
cliente1 = Cliente('marta',30)



#SOLICITANDO DADOS DE OUTRO CLIENTE.
cliente2 = Cliente('jose', 40)

print(f'nome: {cliente1.nome}')
print(f'idade: {cliente1.idade}')

print(f'nome: {cliente2.nome}')
print(f'idade: {cliente2.idade}')