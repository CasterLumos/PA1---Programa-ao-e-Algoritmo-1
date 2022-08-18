# Construa um programa que mostre para o usuário uma lista pré-definida. O usuário deve
# informar duas posições da lista e seu programa deve trocar os valores dessas posições
# e mostrar a lista atualizada.

lista = [1,-2,3,-4,5,6,-7,8,9]
state = 0
print(lista)
posicao1 = int(input('Digite a posição 1'))
posicao2 = int(input('Digite a posição 2'))
state = lista[posicao1]
lista[posicao1] = lista[posicao2]
lista[posicao2] = state

print(lista)

