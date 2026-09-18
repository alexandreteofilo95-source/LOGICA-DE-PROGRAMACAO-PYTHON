import os 
os.system('cls')

# ENTRADA 
usuario= input("digite o nome do usuario: ")
senha = input('digite a sua senha: ')
# PROCESSSAMENTO
if usuario == 'alexandre' and senha == '12345':
    print('bem-vindo')
else: 
    print('usuario ou senha incorreto')

