import os

os.system("cls")

# ENTADA
idade = int(input("Qual sua idade: "))
n = 16,17



# PROCESSMENTO
if idade < 16:
    print("O nao pode")
elif (idade >=16 and idade<=17) or (idade > 65):
    print("o voto e opicional")
elif idade > 18:
    print("o voto e obrigatorio")