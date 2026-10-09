import os 
os.system('cls')

logins = 'marta'
senhas = '@123'
while True:
    login = input('digite seu login: ')
    senha = input('digite sua senha: ')
    
    
    if login == logins and senha == senhas:
        print('ambos estao corretos')
        break
    else:
        print('login ou senha invalidos ')
        print('Tente novamente')
        

    
