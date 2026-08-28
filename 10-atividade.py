import os

os.system("cls")

# ENTRADA
macas = int(input("Quantas maçãs vc deseja: "))
mais = 1.30
menos = 1.00
valor_1 = macas * mais
valor_2 = macas * menos

# PROCESSAMENTO
if macas < 12:
    print(f"elas custam: {valor_1} ")
elif macas >= 12:
    print(f"elas cusaram: {valor_2}")

# FINAL
