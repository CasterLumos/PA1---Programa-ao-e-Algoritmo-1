def organizaLista(lista):
    if lista == []:
        return []
    if list == type (lista[0]) :
        return organizaLista(lista[0]) + organizaLista(lista[1:])
    else :
        return  [lista[0]] + organizaLista(lista[1:])
    
def buscaElemento(lista, elemento):
    if lista:
        novaLista = organizaLista(lista)
        if(novaLista[-1] == elemento):
            return True
        else:
            return buscaElemento(novaLista[:-1], elemento)

elemento = 12
lista = [5, 12, [11,2,45,[55,66,99],77],13,17]
print(buscaElemento(lista, elemento))