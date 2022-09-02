def inverteLista(lista, index = -1, novaLista = []):
    if(len(novaLista)<len(lista)):
        novaLista.append(lista[index])
        return inverteLista(lista, index - 1, novaLista)
    else:
        return novaLista

def rev(l):
    if len(l) == 0: return []
    return [l[-1]] + rev(l[:-1])

print(rev([1,2,3,4,5]))