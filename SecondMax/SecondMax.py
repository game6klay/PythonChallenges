def secondMax(numbers =[2,7,12,78,20]):
    import sys
    maximum = max(numbers)
    x = sys.minint

    for i in numbers:
        if i != maximum:
            if x < i:
                x =i
    print(x)
    return x

def secondMax(numbers):

    import sys
    max1 = sys.minint
    max2 = sys.minint

    for i in numbers:
        if i >= max1:
            max1, max2 = i,max1
        elif i > max2:
            max2 = i

    return max2

def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2