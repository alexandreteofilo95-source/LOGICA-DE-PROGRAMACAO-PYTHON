import os

os.system("cls")

# ENTRADA 
primeiro_numero = int(input("digite um numero: "))
segundo_numero = int(input("digite outro numero: "))


# ENTRADA
soma =  primeiro_numero + segundo_numero
media =  soma / 2
produto = primeiro_numero * segundo_numero
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)


#saida
print(f"\n meidia é igual: {media}")
print(f"O valor da soma é: {soma}")
print(f"O produto é: {produto}")
print(F"maior: {maior}")
print(f"menor: {menor}")

if primeiro_numero == segundo_numero:
    print("Eles sao iguais")
else:
    print(f"maior: {maior}")
    print(f"menor: {menor}")