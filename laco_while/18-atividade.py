import os
os.system('cls')
soma = 0
somaa = 0
somaaa = 0
maior_salario = 0
menor_salario = 9999999
while True:
    print('''
1 | ADICIONAR FAMILIA
2 | SAI E EXIBIR RESULTADOS

''')
    
    digite = input('Digite um numero: ')
    
    match digite:
        case 1:
            salario = float(input('digite seu salario: '))
            numeros = int(input('quantos filhos você tem: '))
            soma += digite
            somaa += salario
            media = somaa / soma
            somaaa +=  numeros
            mediaa = somaaa/ soma
            maior = max(salario, maior_salario)
            menor = min(salario, menor_salario)
            
        case 2:
            print(f'numeros de familias que responderam a pesquisa: {soma}')
            print(f'media de salario da população: {media}')
            print(f'media do numeros de filhos: {mediaa}')
            print(f'maior salario: {maior}')
            print(f'menor salario: {menor}')
            break