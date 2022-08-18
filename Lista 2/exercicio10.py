# Considere uma lista L que possa conter valores repetidos. Formule um programa que
# gere e exiba uma nova lista somente com os valores distintos de L. Por exemplo, para a
# lista L = [1, 3, 5, 1, 2, 3, 5, 5, 2] o programa deve exibir a saída (a lista): [1, 3, 5, 2]

lista = [1, 3, 5, 1, 2, 3, 5, 5, 2] 
listaNova = []

for item in lista:
    if item not in listaNova:
        listaNova.append(item)
        
print(listaNova)