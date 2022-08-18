# Faça um programa que receba uma string e converta todos os seus caracteres para
# maiúsculos. Para facilitar, você pode considerar que a string poderá conter somente os
# seguintes caracteres: ‘a’, ‘b’, ‘c’, ‘z’, x, e ‘g’. Seu programa não pode utilizar as funções# 
# replace e upper

entrada = input('Digite sua frase')
novaFrase = ''
for item in entrada:
    if(item == 'a'):
        novaFrase += 'A'
    if(item == 'b'): 
        novaFrase += 'B'
    if(item == 'c'): 
        novaFrase += 'C'
    if(item == 'z'):  
        novaFrase += 'Z'
    if(item == 'x'):
        novaFrase += 'X'
    if(item == 'g'):
        novaFrase += 'G'
print(novaFrase)