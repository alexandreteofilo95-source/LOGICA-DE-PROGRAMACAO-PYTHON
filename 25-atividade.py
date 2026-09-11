import os 
os.system('cls')

#ENTRADA 

valor = float(input('digite o valor da compra: '))
pagamento = float(input('digite 1 para pagamento a vista e 2 para a prazo: '))
prazo = pagamento
a_vista = valor - 10


#PROCESSAMENTO
match (pagamento):
     case 1:
          print(f'\nO valor do produto: {valor}')
          print('Forma de pagamento: à vista')
          print(f'Valor com desconto: {a_vista}')
          print(f'total pra pagar: {a_vista}')
     case 2:
          print(f'\nvalor do produto: {valor}')
          print(f'Forma de pagamneto: à prazo')
          print('quantdade de parcelas: 6')
          print('Valor por parcela R$ 16,66')
          print(f'total à prazo: {prazo}')
     case _:
          print('digite 1 ou 2')






 