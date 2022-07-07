candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
flag = True
empate = False
vencedor = ''
count = 0
votosNulo = 0
totalVotos = 0

while(flag):
	voto = int(input("Digite um voto:\r\nR:"))
	if(voto < 1 or voto > 5):
		flag = False
	else:
		count = count + 1
	if(voto == 1):
		candidato1 = candidato1 + 1
	elif(voto == 2):
		candidato2 = candidato2 + 1
	elif(voto == 3):
		candidato3 = candidato3 + 1
	elif(voto == 4):
		candidato4 = candidato4 + 1
	else:
		votosNulo = votosNulo + 1

if(candidato1 != 0 and candidato1 >= candidato2 and candidato1 >= candidato3 and candidato1 >= candidato4):
	if(candidato1 == candidato2 or candidato1 == candidato3 or candidato1 == candidato4 ):
		empate = True
	else:
		vencedor = 'Candidato 1'
elif(candidato2 != 0 and candidato1 <= candidato2 and candidato2 >= candidato3 and candidato2 >= candidato4):
	if(candidato1 == candidato2 or candidato2 == candidato3 or candidato2 == candidato4 ):
		empate = True
	else:
		vencedor = 'Candidato 2'
elif(candidato3 != 0 and candidato3 > candidato2 and candidato1 < candidato3 and candidato3 >= candidato4):
	if(candidato1 == candidato3 or candidato2 == candidato3 or candidato3 == candidato4 ):
		empate = True
	else:
		vencedor = 'Candidato 3'
elif(candidato4 != 0 ):
	vencedor = 'Candidato 4'
elif(votosNulo > 0):
	empate = True
else:
	print('voto inválido')

if(not empate and vencedor != ''):
	print('O vencedor foi: {}'.format(vencedor))
elif(empate):
	print('hávera segundo turno')