from ex2 import Media
from ex3 import DesvioPadrao

menorNota = None
maiorNota = 0
file = 'exe_Aula9/notas.txt'
with open(file, 'r')as arquivo:
    for linha in arquivo:
        nota = float(linha.split()[1])
        if(nota>maiorNota):
            maiorNota = nota
        if(menorNota == None or nota < menorNota):
            menorNota = nota

print(menorNota)
print(maiorNota)
print(Media(file))
print(DesvioPadrao(file))