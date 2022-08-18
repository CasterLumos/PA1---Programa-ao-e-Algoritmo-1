# Assuma duas listas de tamanhos iguais. A primeira lista (L1) contém valores únicos
# (chaves) enquanto a segunda lista (L2) contém valores arbitrários. Construa um
# dicionário usando a primeira lista como as chaves e a segunda como os valores. Por
# exemplo, para as listas L1 = [1.87, 1.95, 0.76] e L2 = ['z', 'a', 'b'] o programa deve gerar o
# seguinte dicionário {1.87: 'z', 1.95: 'a', 0.76: 'b'}.

l1 = [1.87, 1.95, 0.76]
l2 = ['z', 'a', 'b']
dict1 = {}

for i in range(len(l1)):
    dict1[l1[i]] = l2[i]

print(dict1)