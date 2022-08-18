# Assuma uma lista de n elementos. Faça um programa onde o usuário digite uma posição
# dessa lista e, se a posição digitada for válida, o programa exibe o elemento da posição
# digitada

listaExemplo = [1,2,3,4,5,6,7,8,9]

entrada = int(input('Digite uma posição da lista a seguir: {}'.format(listaExemplo)))

if(entrada >= 0 and entrada < len(listaExemplo)):
    print(listaExemplo[entrada])