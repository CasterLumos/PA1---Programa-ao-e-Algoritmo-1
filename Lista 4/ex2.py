string = input('Digite uma String')
letra2 = input('Digite um Caractere')
count = 0
for letra in string:
    if(letra == letra2):
        count += 1

print('A letra \'{}\' aparece {} vezes na frase!'.format(letra2, count))