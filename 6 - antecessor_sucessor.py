import os

#Limpa o terminal.
os.system("cls")

print(" = SOLICITANDO DADOS =")
numero = int(input("digite um numero inteiro: "))

# CALCULANDO.
antecessor = numero - 1
sucessor = numero + 1
print("\n = EXIBINDO DADOS =")

print("O numero: ", numero)
print("o antecessor é: ", antecessor)
print("o sucessor é: ", sucessor)