import os 
os.system('cls')

# ENTRADA 
sexo = input('Qual seu sexo: ')
ano = int(input('Qual ano que voçê nasceu: '))
data = 2026
# PROCESSAMENTO
soma = data - ano
if sexo == 'Masculino' and (ano >= 18 or ano < 65):
    print('voce deve se apresentar ao serviço militar')
else:
    print('não deve se apresentar')