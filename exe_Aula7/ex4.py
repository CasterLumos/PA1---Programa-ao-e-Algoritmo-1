def misturaLista(lista1, lista2):
    listaFinal = []
    for index in range((len(lista1)+len(lista2))):
        if index < len(lista1):
            listaFinal.append(lista1[index])
            listaFinal.append(lista2[index])
    return listaFinal

# print(misturaLista([0,2,4,6,8], [1,3,5,7,9]))