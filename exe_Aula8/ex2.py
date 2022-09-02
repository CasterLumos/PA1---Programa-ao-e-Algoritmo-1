
def primoNumero(num, index = 2):
    if(index == num):
        return True
    elif(num % index == 0):
        return False
    return primoNumero(num, index + 1)

print(primoNumero(4))