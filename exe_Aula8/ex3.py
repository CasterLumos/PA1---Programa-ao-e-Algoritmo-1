def multiplicacao(num1, num2):
    if(num2 == 0):
        return 0
    elif(num2 < 0):
        return -num1 + multiplicacao(num1, num2+1)
    else:
        return num1 + multiplicacao(num1, num2-1)

print(multiplicacao(0, 1))