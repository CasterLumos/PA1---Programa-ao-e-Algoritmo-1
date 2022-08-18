countFriends = int(input('Quantidade de amigos'))
tuplas = []
menorIdade = maiorAltura = None
for amigo in range(countFriends):
    nome = input('Qual seu nome')
    idade = int(input('Qual sua idade'))
    altura = int(input('Qual sua altura '))
    tupla = (nome, idade, altura)
    print(tupla)
    tuplas.append(tupla)

for tupla in tuplas:
    idade = tupla[1]
    altura = tupla[2]
    if(menorIdade == None or menorIdade > idade):
        menorIdade = idade
    if(maiorAltura == None or maiorAltura < altura):
        maiorAltura = altura
    
print('A menor idade  é: {} e a maior altura é {} '.format(menorIdade, maiorAltura))

