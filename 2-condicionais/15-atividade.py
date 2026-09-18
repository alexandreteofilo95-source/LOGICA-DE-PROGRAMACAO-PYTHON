import os
os.system('cls')

# ENTRADA
peso = float(input("digite seu peso: "))
altura = float(input('digite sua altura: '))

# PROCESSAMENTO.

imc = peso / (altura * altura)
print(f'\nSeu indice de massa corporal (IMC) é: {imc}')

if imc < 18.5:
    print('abaixo do peso')
elif imc == 18.6 or imc == 24.9:
    print('peso ideal(parabéns)')
elif imc == 25.0 or imc <= 29.0:
    print('levemente acima do peso')
elif imc ==30.0 or imc <= 34.9:
    print('obesidade grau 1')
elif imc == 35.0 or imc <= 39.9:
    print('obesidade grau 2 (severa)')
else:
    print('obesidade grau 3 (morbida)')