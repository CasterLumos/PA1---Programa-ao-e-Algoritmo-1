from ex1 import somaLista

def listaSubtração(lista, numero = 0):
    listaFinal = []
    if(numero == 0):
        numero = somaLista(lista)/len(lista)
    for numeroLista in lista:
        listaFinal.append(numeroLista - numero)
    
    
    return listaFinal

#print(listaSubtração([1,2,3,4,5,6,7,8,9], 1))
