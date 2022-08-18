# Elabore um programa que percorra uma lista de valores inteiros positivos e coloque os
# valores das posições ímpares em uma nova lista e a exiba.

lista = [1,2,3,4,5,6,7,8,9]
listaImpares = []
count = 0

while count < len(lista)-1:
    if(count%2 != 0):
        listaImpares.append(lista[count])
    count += 1

print(listaImpares)