# Elabore um programa que solicite ao usuário inserir vários valores inteiros (positivos e
# negativos). O programa encerra a solicitação de valores quando o usuário insere o valor
# -1. Os valores positivos devem ser armazenados em uma lista e, ao final, seu programa
# deve exibir esta lista

lista = []

flag = True

while(flag):
    entrada = int(input("Insira valores inteiros"))
    if(entrada == -1):
        flag = False
    else:
        lista.append(entrada)

print(lista)