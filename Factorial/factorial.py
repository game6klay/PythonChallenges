def FirstFactorial(num):
    factorial = 1

    for i in range(1, num + 1):
        # multiply each number between 1 and num
        # factorial = 1 * 1 = 1
        # factorial = 1 * 2 = 2
        # factorial = 2 * 3 = 6
        # factorial = 6 * 4 = 24
        # ...
        factorial = factorial * i

    return factorial
