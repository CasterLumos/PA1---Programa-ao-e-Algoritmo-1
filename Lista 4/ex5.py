# Formule um programa que verifique se uma string é uma palavra palíndromo. Uma
# palavra palíndromo é uma palavra que pode ser lida da esquerda para direita e vice-
# versa com o mesmo sentido. Por exemplo, “ana”, “renner” e “TENET” são exemplos de
# palíndromos.

nome = "TENET"
nomeInvertido = ''

for index in range(len(nome)):
    nomeInvertido += (nome[-(index + 1)])

if(nome == nomeInvertido):
    print("É palindromo")
else:
    print("Não é palindromo")