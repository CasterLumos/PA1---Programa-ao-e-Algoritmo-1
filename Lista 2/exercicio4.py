# Elabore um programa que subtraia todos os elementos de uma lista pelo valor médio
# dos elementos compondo a lista

lista = [1,1, 1, 1] 
soma = 0
count = 0

for item in lista:
    soma += item

while count < len(lista):
    lista[count] -= (soma)/len(lista)
    count += 1

print(lista)