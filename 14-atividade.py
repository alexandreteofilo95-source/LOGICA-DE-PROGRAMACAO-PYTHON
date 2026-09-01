import os 
os.system("cls")

# ENTRADA 
nome = input("Nome do aluno: ")
primero_numero = float(input("Digite a primeia nota: "))
segunda_numero = float(input("Digite a segunda nota: "))
media = (primero_numero + segunda_numero) / 2



print(f"\n nome: {nome}")
print(f"Primeira nota: {primero_numero}")
print(f"Segunda nota: {segunda_numero}")
print(f"Media: {media}")


if media >= 6:
    print("aprovado")
else: 
    print("reprovado")
