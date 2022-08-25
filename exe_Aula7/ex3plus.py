# Quantos números primos o usuário quer
from ex3 import isPrimeNumber

listaPrimos = []
quantidadeNumeros = 100
numero = 2

while len(listaPrimos) < quantidadeNumeros:
    if(isPrimeNumber(numero)):
        listaPrimos.append(numero)
    numero += 1

print(listaPrimos)

# Quantos números primos até uma entrada

entrada = 100
listaPrimos2 = []
for numero in range(2, entrada):
    if(isPrimeNumber(numero)):
        listaPrimos2.append(numero)

print(len(listaPrimos2))