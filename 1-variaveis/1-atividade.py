import os

# LIMPANDO O TERMINAL
os.system("cls")
print("= SOLICITANDO DADOS =")
primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("digite o segundo numero: "))

# PROCESSAMENTO.
soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

# SAIDA DE DADOS
print("\n = EXIBINDO DADOS =")
print("A soma é: ", soma)
print("A subtração é: ", subtracao)
print("A multiplicação é: ", multiplicacao)
print("A divisão é: ", divisao)
