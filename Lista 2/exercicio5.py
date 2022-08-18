# Construa um programa que percorra uma lista de valores inteiros positivos e coloque os
# valores pares e ímpares em duas novas listas (uma lista somente para os pares e uma
# para os ímpares). Ao final seu programa deve exibir a lista de pares e a lista de ímpares.

lista = [1,2,3,4,5,6,7,8,9]
listaPar = []
listaImpar = []

for item in lista:
    if item % 2 == 0:
        listaPar.append(item)
    else:
        listaImpar.append(item)

print(listaImpar)
print(listaPar)