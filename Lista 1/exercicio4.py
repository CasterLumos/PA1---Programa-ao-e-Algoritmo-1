# Construa um programa que solicite ao usuário entrar com valores inteiros (positivos e
# negativos). O programa deve imprimir quantos números positivos e maior que zero o
# usuário inseriu (digitou). O programa encerra a solicitação de valores quando o usuário
# inserir o caractere ‘p’.

digitouP = True
count = 0
while(digitouP):
    entrada = input("digite um número")
    if(entrada == 'p'):
        digitouP = False
    elif(int(entrada) > 0):
        count = count + 1
print('A quantidade de vezes que digitou um número positivo é {}'.format(count))
