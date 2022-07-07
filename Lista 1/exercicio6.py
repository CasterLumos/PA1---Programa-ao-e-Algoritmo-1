# Escreva um programa que mostre a soma de todos os números pares e a soma de todos
# números ímpares existentes entre um intervalo de números inteiros fornecidos pelo
# usuário. Por exemplo, se o usuário entrar com o intervalo 1-5 o programa deverá exibir
# a seguinte saída: Soma par 6, soma ímpar 9.

entradaInicio = int(input('Digite o primeiro número: '))
entradaFim = int(input('Digite o último número: '))
somaPar = 0
somaImpar = 0
if(entradaInicio >= entradaFim):
    print('Entradas inválidas')
else:
    for element in range(entradaInicio, entradaFim+1, 1):
        if element % 2 == 0:
            somaPar = somaPar + element
        else:
            somaImpar = somaImpar + element
print('Soma par {}, soma ímpar {}'.format(somaPar, somaImpar))
