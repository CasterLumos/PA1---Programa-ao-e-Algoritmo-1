# Elabore um programa que solicite ao usuário entrar com uma string e com dois
# caracteres. O programa deve trocar toda a ocorrência do primeiro caractere pelo
# segundo na string. Por exemplo, para a entrada “programação”, “a” “z” o programa
# deve exibir a seguinte saída: “progrzmzção”

nome = input("Digite uma palavra")
letra = input('Digite a letra a ser substituida de {}:\r\nR:'.format(nome))
letra2 = input('Digite a letra a ser substituida em {}, no lugar de {}:\r\nR:'.format(nome, letra))

novoNome = nome.replace(letra, letra2)

print(novoNome)

