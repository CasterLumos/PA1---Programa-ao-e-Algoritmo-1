# Faça um programa que receba a idade, peso e altura de uma pessoa. O programa deve
# exibir o Índice de Massa Corporal (IMC) da pessoa e informar se ela é maior de idade ou
# não. (Fórmula do IMC: Peso/Altura^2).

idade = int(input('Qual sua idade'))
altura = float(input('Qual sua altura'))
peso = int(input('Qual seu peso'))
imc = peso / altura**2
print('Seu imc é {:.2f}'.format(imc))
maioridade = 'Maior de idade' if idade >= 18 else 'menor de idade'
print(maioridade)
