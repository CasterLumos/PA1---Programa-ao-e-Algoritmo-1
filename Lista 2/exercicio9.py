# Elabore um programa que mostre se duas listas contêm os mesmos valores. A ordem
# em que os valores estão nas listas não importa. Seu programa deve considerar que lista
# armazena somente valores inteiros e os valores em uma lista são distintos. Por exemplo,
# para as listas [1, 3, 4, 2] e [1, 2, 3, 4] seu programa deve indicar que as listas são iguais.
# Por outro lado, para as listas [8, 7, 3, 1] e [7, 3, 1, 2] seu programa deve indicar que as
# listas são diferentes. Neste programa você não pode utilizar as instruções break e nem
# continue do Python.

lista1 = [1, 4, 3, 2]
lista2 = [4, 3, 2, 1]
count = 0
equals = 0
equals2 = 0
if(len(lista1) == len(lista2)):
    for item in lista2:
        while count < len(lista1):
            if(item == lista1[count]):
                equals += 1
            count += 1
        count = 0
    for item in lista1:
        while count < len(lista1):
            if(item == lista2[count]):
                equals2 += 1
            count += 1
        count = 0
else:
    print('As listas não tem o mesmo tamanho')

if(equals == len(lista1) and equals == len(lista1)):
    print('Listas semelhantes')
else:
    print('As listas são diferentes')