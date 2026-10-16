import os
os.system('cls')
positivo = 0
numeros_vetores = []
soma = 0
negativo = 0
NUMEROS_TENTATIVAS = 5
for i in range(NUMEROS_TENTATIVAS):
    numero = int(input(f'Digite {i+1}º numero: '))
    numeros_vetores.append(numero)
    if numero > 0:
        soma +=numero
    else:
        negativo +=1
print(f'Soma dos positivos: {soma}')
print(f'numeros negativos: {negativo}')