import os
os.system('cls')

while True:
    print('crie seu login e senha')
    lo = input('\ndigite seu login: ')
    se = input('Digite sua senha: ')
    os.system('cls')

    print('digite o login e a senha criado')
    login = input('\nDigite seu login: ')
    senha = input('digite sua senha: ')
    if lo == login and se == senha:
        print('Bem-vindo')
        break
    else:
        print('Login ou senha invalidos!')
        input('Aperte Enter para voltar...')
        os.system('cls')
