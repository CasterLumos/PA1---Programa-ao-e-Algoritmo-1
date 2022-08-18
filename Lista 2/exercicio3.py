# Formule um programa que mostre a soma de todos os elementos de uma lista. Por
# exemplo, para a lista a = [3, 7, 5, 0] seu programa deve mostra a saída: 15.

lista = [3, 7, 5, 0] 
soma = 0

for item in lista:
    soma += item

print(soma)