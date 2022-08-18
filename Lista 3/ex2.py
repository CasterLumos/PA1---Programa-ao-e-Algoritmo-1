countFriends = int(input('Quantidade de amigos'))
tuplas = []
menorIdade = maiorAltura = nomeIdade = nomeAltura =  None
for amigo in range(countFriends):
    nome = input('Qual seu nome')
    idade = int(input('Qual sua idade'))
    altura = int(input('Qual sua altura '))
    tupla = (nome, idade, altura)
    print(tupla)
    tuplas.append(tupla)

for tupla in tuplas:
    nome = tupla[0]
    idade = tupla[1]
    altura = tupla[2]
    if(menorIdade == None or menorIdade > idade):
        menorIdade = idade
        nomeIdade = nome
    if(maiorAltura == None or maiorAltura < altura):
        maiorAltura = altura
        nomeAltura = nome
    
print('A menor idade  é: {}  do {} e a maior altura é {} do {} '.format(menorIdade, nomeIdade, maiorAltura, nomeAltura))

