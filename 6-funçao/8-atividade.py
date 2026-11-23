import os
os.system('cls')

def inflacao(preco):
    if preco < 100:
        inflacao = preco * 1.10
    elif preco >= 100:
        inflacao = preco * 1.20
    return inflacao

preco = int(input('coloque o valor do produto: '))

inflacao = inflacao(preco)
print('\n = EXIBINDO RESULTADO =')
print(f'preço do produto: {preco} e com inflação: {inflacao}')
