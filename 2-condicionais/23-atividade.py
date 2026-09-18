import os
os.system('cls')

dia = input('Digite o dia da semana: ').lower().upper()
match dia: 
    case 'segunda' | 'SEGUNDA':
        print('Segunda é um dia útil')
    case 'terça' | 'TERÇA':
        print('Terça é um dia util')
    case 'quarta' | 'QUARTA':
        print('quarta-feira é um dia util')
    case 'quinta' | 'QUINTA':
        print('quinta-feira é um dia util')
    case 'sexta' | 'SEXTA':
        print('secta-feira é um dia util')
    case 'sábado' | 'sabado' | 'domingo' :
        print('final de semana não é dia util')
    case _: 
        print('Dia invalido')
print(dia)

print('==== fim ====')