import os 
os.system('cls')

#ENTRADA 
print('== aviso'

' ==')
valor = float(input('digite o valor da compra: '))
pagamento = int(input('digite 1 para pagamento a vista e 2 para a prazo: '))
parcelado_x2 = pagamento / 2
parcelado_x3 = pagamento / 3
parcelado_x4 = pagamento / 4
parcelado_x4 = pagamento / 5
parcelado_x5 = pagamento / 6
prazo = pagamento
a_vista = pagamento * 0.10

#PROCESSAMENTO

match pagamento:
    case 1:
        print(f'vai ficar: {a_vista}')
    case 2:
        print(f'vai ficar: {prazo}')
    case _:
        print('coloque o numero 1 ou 2')
print(pagamento)
print('== fim ==')


