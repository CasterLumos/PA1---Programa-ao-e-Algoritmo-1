# Faça um programa onde o usuário informe uma string e um valor inteiro n. O programa
# deve gerar uma nova string com a string informada pelo usuário concatenada n vezes.
# Por exemplo, se o usuário digitar “abc” e o valor 3 o programa deve exibir: “abcabcabc”.

nome = input("Qual a palavra")
quantidade = int(input("Digite um inteiro"))
novoNome = ''

# novoNome = nome * int(input('Quantas vezes quer repetir o {}?'.format(nome)))

for item in range(quantidade):
    novoNome += nome


print(novoNome)