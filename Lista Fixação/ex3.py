# Elabore um programa onde o usuário digita uma string e, em seguida, um caractere. O
# programa deve contar quantas vezes esse caractere aparece na string. Por exemplo, se
# o usuário digitar a string “Programação e Algoritmos I” e o caractere ‘a’ o programa deve
# exibir a saída 2.

frase = input('Digite sua frase')
caractere = input('Digite um caractere')
count = 0
for item in frase:
    if(item == caractere):
        count += 1

print(count)