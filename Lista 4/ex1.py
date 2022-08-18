# Construa um programa que solicite ao usuário entrar com seu nome completo. Em
# seguida, o programa deve exibir somente o primeiro e o último nome do usuário. Dica
string = input('Digite seu nome completo')

print('O seu nome é: {} {}'.format(string.split()[0],string.split()[-1]))
