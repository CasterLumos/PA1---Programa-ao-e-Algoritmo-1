# Faça um programa onde o usuário entra com o número de linhas e colunas de uma
# matriz. Em seguida, seu programa deve solicitar que o usuário digite os valores para
# povoar essa matriz.

linhas  = int(input('Digite o número de linhas '))
colunas = int(input('Digite o número de colunas '))
matriz = []
line = []

for linha in range(linhas):
    for coluna in range(colunas):
        line.append([])
    matriz.append(line)
    line = []

for linha in range(linhas):
    for coluna in range(colunas):
        matriz[linha][coluna].append(int(input('Digite um número')))

print(matriz)