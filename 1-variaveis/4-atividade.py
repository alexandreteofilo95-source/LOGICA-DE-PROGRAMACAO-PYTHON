import os
os.system ("cls")

# ENTRADA
primeiro_numero = float(input("digite um numero: "))
segundo_numero = float(input("digite outro numero: "))
terceiro_numero = float(input("digite outro numero de novo: "))

maior = max(primeiro_numero, segundo_numero, terceiro_numero)
menor = min(primeiro_numero, segundo_numero, terceiro_numero)

print(f"\nO primeiro numero é: {primeiro_numero} ") 
print(f"O segundo numero é: {segundo_numero}")
print(f"O terceiro numero é: {terceiro_numero}")
print(f"O maior é: {maior}")
print(f"O menor é: {menor}")
