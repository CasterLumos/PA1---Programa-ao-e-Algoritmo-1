print("Para votar no primeiro candidato digite: 1 \nPara votar no segundo candidato digite: 2 \nPara votar no terceiro candidato digite: 3 \nPara votar no quarto candidato digite: 4")
a=int(input("Digite um número "))
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
#contk=0
#contg=0
#contp=0
#contf=0
#contkk=0
if a==1:
    cont1=1
    while a==1 or a==2 or a==3 or a==4 or a==5:
        a=int(input("Digite um número "))
        if a==1:
            cont1+=1
            #contk+=cont1
        if a==2:
            cont2+=1
            #contg+=cont2
        if a==3:
            cont3+=1
            #contp+=cont3
        if a==4:
            cont4+=1
            #contf+=cont4
        if a==5:
            cont5+=1
elif a==2:
    cont2=1
    while a==1 or a==2 or a==3 or a==4 or a==5:
        a=int(input("Digite um número "))
        if a==1:
            cont1+=1
            #contk+=cont1
        if a==2:
            cont2+=1
            #contg+=cont2
        if a==3:
            cont3+=1
            #contp+=cont3
        if a==4:
            cont4+=1
        if a==5:
            cont5+=1
elif a==3:
    cont3=1
    while a==1 or a==2 or a==3 or a==4 or a==5:
        a=int(input("Digite um número "))
        if a==1:
            cont1+=1
            #contk+=cont1
        if a==2:
            cont2+=1
            #contg+=cont2
        if a==3:
            cont3+=1
            #contp+=cont3
        if a==4:
            cont4+=1
        if a==5:
            cont5+=1
elif a==4:
    cont4=1
    while a==1 or a==2 or a==3 or a==4 or a==5:
        a=int(input("Digite um número "))
        if a==1:
            cont1+=1
            #contk+=cont1
        if a==2:
            cont2+=1
            #contg+=cont2
        if a==3:
            cont3+=1
            #contp+=cont3
        if a==4:
            cont4+=1
        if a==5:
            cont5+=1
elif a==5:
    cont5=1
    while a==1 or a==2 or a==3 or a==4 or a==5:
        a=int(input("Digite um número "))
        if a==1:
            cont1+=1
            #contk+=cont1
        if a==2:
            cont2+=1
            #contg+=cont2
        if a==3:
            cont3+=1
            #contp+=cont3
        if a==4:
            cont4+=1
        if a==5:
            cont5+=1
contvalidos = cont1 + cont2 + cont3 + cont4
if cont1> cont2 and cont1>cont3 and cont1>cont4:
    print("Primeiro candidato venceu")
elif cont2> cont1 and cont2> cont3 and cont2>cont4:
    print("Segundo candidato venceu")
elif cont3> cont1 and cont3> cont2 and cont3>cont4:
    print("Terceiro candidato venceu")  
elif cont4> cont1 and cont4> cont2 and cont4>cont3:
    print("Quarto candidato venceu")  
elif cont4== cont1 and cont4> cont2 and cont4>cont3:
    print("Haverá segundo turno entre o primeiro e o quarto candidato")  
elif cont4== cont2 and cont4> cont1 and cont4>cont3:
    print("Haverá segundo turno entre o segundo e o quarto candidato")  
elif cont4== cont3 and cont4> cont2 and cont4>cont1:
    print("Haverá segundo turno entre o terceiro e o quarto candidato")  
elif cont1== cont2 and cont1> cont3 and cont1>cont4:
    print("Haverá segundo turno entre o primeiro e o segundo candidato")  
elif cont1== cont3 and cont1> cont2 and cont1>cont4:
    print("Haverá segundo turno entre o primeiro e o terceiro candidato")
elif cont2== cont3 and cont2> cont1 and cont2>cont4:
    print("Haverá segundo turno entre o segundo e o terceiro candidato")
elif cont5> cont1 and cont5>2 and cont5>cont3 and cont5>cont4:
    print("Ninguem venceu, pois houve mais votos nulos do que para um candidato especifico, deste modo será preciso uma nova eleição")
    
print("Quantidade de votos para o primeiro candidato: ",cont1)
print("Quantidade de votos para o segundo candidato: ",cont2)
print("Quantidade de votos para o terceiro candidato: ",cont3)
print("Quantidade de votos para o quarto candidato: ",cont4)
print("Quantidade de votos nulos: ",cont5)
print("Quantidade de votos não nulos: ",contvalidos)