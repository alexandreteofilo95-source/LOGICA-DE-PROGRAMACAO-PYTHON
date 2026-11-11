import os
os.system('cls')
NUMEROS_TENTATIVAS = 3
lista_produtos = []
def pedindo_dados():
    for i in range(3):
        produto = input('digite o nome do produto: ')
        lista_produtos.append(produto)

def mostrar_dados(lista_produtos):
    for i in range(NUMEROS_TENTATIVAS):
        print(f'{i+1} - {lista_produtos[i]}')

print('= SOLICITANDO DADOS =')
pedindo_dados()

print('\n= EXIBINDO DADOS =')
mostrar_dados(lista_produtos)