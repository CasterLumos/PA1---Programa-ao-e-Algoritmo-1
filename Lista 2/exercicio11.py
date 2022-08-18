# Escreva um programa que mostre os valores de uma lista aos pares, onde o primeiro
# elemento faz par com o último, o segundo com o penúltimo, e assim por diante. Por
# exemplo, para a lista L = [1, 4, 5, 10, 8, 7] o programa deve exibir a seguinte saída: ‘1 7’,
# ‘4 8’, ‘5 10’. Note que para este propósito, a lista deve ter um número par de elementos.
# Caso a lista não satisfaça essa característica, o programa deve replicar o elemento do
# meio lista e colocá-lo no final da lista. Em seguida, o programa deve fazer a exibição aos
# pares. Por exemplo, para os valores armazenados [1, 4, 5, 10, 8] o programa deve exibir
# ‘1 5’, ‘4 8’, ‘5, 10’.

lista = [1, 4, 5, 10, 8]
listaNova = []
count = 0 

if(len(lista)%2 != 0):
    lista.append(lista[int(len(lista)/2)])


limit = int(len(lista)/2)

while count < limit:
    listaNova.append('{} {}'.format(lista[count], lista[-count-1]))
    count += 1

print(listaNova)