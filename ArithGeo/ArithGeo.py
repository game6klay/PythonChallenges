def typeOfSequence(array):

    diff = array[0] - array[1]
    times = array[1]/array[0]
    arithmetic = True

    for i in range(0, len(array)-1):
        if diff != array[i+1] - array[i]:
            arithmetic= False
            break

    if arithmetic:
        return "Arithmetic"

    for i in range(0, len(array)-1):
        if times != (array[i+1]/array[1]):
            return -1

    return "Geometric"
