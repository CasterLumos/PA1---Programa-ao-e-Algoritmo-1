# Elabore um programa que exiba todos os números inteiros entre dois intervalos (inteiros
# positivos) fornecidos pelo usuário. Por exemplo, se o usuário inserir o intervalo 21-30 o
# programa deve exibir a seguinte saída: 21, 22, 23, 24, 25, 26, 27, 28, 29, 30. O programa
# deve garantir que o usuário inseriu intervalos válidos (intervalo 1 menor que intervalo
# 2); caso contrário, o programa deve exibir a mensagem “Intervalo inválido”.
entradaInicio = int(input('Digite o primeiro número: '))
entradaFim = int(input('Digite o último número: '))
if(entradaInicio >= entradaFim):
    print('Entradas inválidas')
else:
    for element in range(entradaInicio, entradaFim+1, 1):
        print(element)
