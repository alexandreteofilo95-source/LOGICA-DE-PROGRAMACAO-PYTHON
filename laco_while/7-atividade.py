import os
os.system('cls')
NUMEROS_TENTATIVAS = 3
logins = 'marta'
senhas = '@123'
for i in range (NUMEROS_TENTATIVAS):
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    if login == logins and senha == senhas:
        print('bem-vindo')
    else:
        print(f'você so tem {i-NUMEROS_TENTATIVAS}')
        input('prissione para voltar...')
        os.system('cls')
