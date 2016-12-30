def isPrime (number):
    num = int(number)
    x = True
    for i in range(2,num+1):
        if (num%i == 0):
            return False
        else:
            return True

    if x:
        print
        "prime"
    else:
        print
        "not prime"