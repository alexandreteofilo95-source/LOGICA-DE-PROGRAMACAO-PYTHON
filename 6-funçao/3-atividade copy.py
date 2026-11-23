import os
os.system('cls')
def logo_senai():
    print('='*15)
    print('      SENAI')
    print('='*15)
def mostrar_dados():
    print(f'nome: {nome}, email: {email}, telefone: {telefone}')

logo_senai()
print('\n = Solicitando dados =')
nome = input('digite seu nome: ')
email = input('digite seu email: ')
telefone = input('digite seu telefone: ')

logo_senai()
print('\n = exibindo dados =')
mostrar_dados()
