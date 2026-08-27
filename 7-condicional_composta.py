import os

os.system("cls")

# ENTRADA
primera_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))  
terceira_nota = float(input("Digite a terceira nota: "))

# PROCESSAMENTO
media = (primera_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    resultado = "aprovado"
else:
    resultado = "reprovado"
    

# SAIDA
print(f "media: {aprovado}")
print (f"media: {reprovado}")

