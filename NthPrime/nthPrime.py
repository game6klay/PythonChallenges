def isPrime (number):
    num = int(number)
    x = True
    for i in range(2,num+1):
        if (num%i == 0):
            return False
        else:
            return True

def nthPrime(n):

    import sys
    counter =0
    num = None
    for i in range(0, sys.maxint):
        if counter > n:
            num = i
            break
        if isPrime(i):
            counter+=1

    return num



# Alternate solution

def PrimeMover(n):
    primeArray =[]
    for num in range(1,10**4):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
            primeArray.append(num)
    print
    primeArray[n]

PrimeMover(16)