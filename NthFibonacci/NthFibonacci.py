def nthFibonacci(num):


    if num == 0 or num == 1:
        return num
    else:
        return nthFibonacci(num-1) + nthFibonacci(num-2)



