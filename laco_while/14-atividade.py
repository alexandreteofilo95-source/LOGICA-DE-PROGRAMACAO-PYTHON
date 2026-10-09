import os
os.system('cls')

contador = 3
while True:
    primeira = float(input('Digite uma nota: '))
    segunda = float(input('Digite uma nota: '))
    outra = input('Quer digitar outra nota: ')
    match outra:
        case 'SIM' | 'sim':
            teiceira = int(input('Digite sua outra nota: '))
            print(f'Sua 1º nota foi: {primeira}')
            print(f'Sua 2º nota foi: {segunda}')
            print(f'Sua 3º nota foi: {teiceira}')
            break
        case 'NÃO' | 'não':
            soma = (primeira + segunda) / 2
            print(f'\nsua media: {soma}')
            print(f'Sua 1º nota: {primeira}')
            print(f'Sua 2º nota: {segunda}')
            print(f'quantidades de inteirações: {contador}')
            break

        