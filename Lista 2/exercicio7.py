# Considere uma lista que armazene valores inteiros. Crie um programa que indique a
# quantidade valores positivos e negativos que a lista está armazenando.

lista = [1,-2,3,-4,5,6,-7,8,9]
count = 0

for item in lista:
    if(item > 0):
        count += 1

print('A quantidade de números positivos é {} e negativos é {} '.format(count, len(lista)-count))

