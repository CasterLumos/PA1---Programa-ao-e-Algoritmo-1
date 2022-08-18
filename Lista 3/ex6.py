lista = ['a', 1, 'b', 2, 'c', 3]
dict1 = {}
for i in range(int(len(lista)/2)):
    dict1[lista[2*i]] = lista[2*i+1]

print(dict1)