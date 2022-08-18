#Elabore um programa que conte quantos caracteres distintos existem em uma string.

nome = "sasadodorrrcccc"
dic = {}


for caracter in nome:
    if caracter in dic:
        dic[caracter] += 1
    else:
        dic[caracter] = 1


print(dic)