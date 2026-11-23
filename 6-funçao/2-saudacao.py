import os
os.system('cls')
def mostrar_saudacao(nome,idade):
    print(f'{nome} tem {idade} anos')
print('= solicitando dados =')
nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

print('\n= EXIBINDO DADOS =')
mostrar_saudacao(nome,idade)