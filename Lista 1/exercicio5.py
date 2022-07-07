# Faça um programa que mostre os números pares existentes entre um intervalo de
# números fornecidos pelo usuário. Por exemplo, se o usuário informar o intervalo 1-7 o
# programa deve exibir a seguinte saída: 2, 4, 6.

entradaInicio = int(input('Digite o primeiro número: '))
entradaFim = int(input('Digite o último número: '))
if(entradaInicio >= entradaFim):
    print('Entradas inválidas')
else:
    for element in range(entradaInicio, entradaFim+1, 1):
        if element % 2 == 0:
            print(element)  
