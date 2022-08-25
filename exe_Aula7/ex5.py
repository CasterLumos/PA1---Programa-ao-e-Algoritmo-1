def maiorDaListas(lista1, lista2):
    maior1 = 0
    maior2 = 0
    for numero in lista1:
        if(numero > maior1):
            maior1 = numero
    for numero2 in lista2:
        if(numero2 > maior2):
            maior2 = numero2
    if(maior1 > maior2):
        return maior1
    return maior2


def calculadoraMaluca(lista1, lista2, operacao = 0):
    listaFinal = []
    if(not operacao):
        return maiorDaListas(lista1, lista2)
    for i in range(len(lista1)):
        if(operacao):
                listaFinal.append((lista1[i]+(lista2[i])))
        elif(operacao == 2):
                listaFinal.asppend((lista1[i]-(lista2[i])))
        elif(operacao == 3):
                listaFinal.append((lista1[i]*(lista2[i])))
        elif(operacao == 4):
                listaFinal.append((lista1[i]/(lista2[i])))
    return listaFinal

print(calculadoraMaluca([1,2,3,4,5], [1,2,3,4,5]))