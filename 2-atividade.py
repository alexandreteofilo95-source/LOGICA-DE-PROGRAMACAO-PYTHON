import os

# LIMPANDO O TERMINAL
os.system("cls")
print("= SOLICITANDO DADOS =")
salario = float(input("digite o salario de um funcionario: "))


# PROCESSAMENTO
print("\n = EXIBINDO DADOS =")
divisao = salario / 1621

# SAIDA
print(f"O funcionario recebe: {divisao} vezes o salario minimo.")