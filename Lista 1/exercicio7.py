# Escreva um programa que leia um número inteiro positivo (maior que um) e determine
# se ele é primo. Dica: a instrução n%m==0 indica que o resto da divisão de n por m é zero
# (operação módulo).
flag = False

num1 = int(input('número:'))
for element in range(2, num1):
    if(num1 % element == 0):
        flag = True
if(not flag):
    print('É primo')
else:
    print('nao é primo')
