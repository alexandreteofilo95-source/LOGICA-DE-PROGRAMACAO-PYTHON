import os
os.system('cls')
quantidade = 0
soma =0
maior_idade = 0
menor_idade = 99999
while True:
    print('''
1 | ADICIONAR PESSOA
2 | EXIBIR RESULTADOS
3 | SAIR
''')
    digite = int(input('escolha: '))
    match digite:
        case 1:
            idade = int(input('Digite sua idade: '))
            sexo = input('Qual seu sexo(M/F): ')
            salario = float(input('Qual seu salario): '))
        case 2:
            quantidade += digite
            soma += salario
            media = salario / quantidade
            print(f'Media de salario: {media}')
            maior = max(idade, maior_idade)
            menor = min(idade,menor_idade)
            print(f'maior: {maior} e menor: {menor} idade')
            


            