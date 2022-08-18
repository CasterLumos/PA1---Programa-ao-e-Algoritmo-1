#Construa um programa que solicite ao usuário informar quantos valores inteiros ele irá
#inserir. Após isso, programa “força” o usuário a digitar essa quantidade de valores que
#devem ser inseridos em uma lista. Ao final, o programa exibe a lista e o menor elemento
#da lista. Observação: o menor elemento deve ser encontrado percorrendo a lista e não
#no momento em que o usuário está digitando os valores

quantidade = int(input('Quantos números'))
count = 0 
lista = []
valorMinimo = None

while(count < quantidade):
    lista.append(int(input('Digite um número')))
    count += 1

for item in lista:
    if(valorMinimo is None or item < valorMinimo):
        valorMinimo = item




print('A lista é {} e o menor valor é: {} '.format(lista, valorMinimo))