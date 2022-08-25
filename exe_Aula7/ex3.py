def isPrimeNumber(number):
    flag = None
    for element in range(2, number):
        if(number % element == 0):
            return False
    return True

#print(isPrimeNumber(3))




