def ABCheck(aString):
    for i in range(len(aString)):
        if aString[i] == "a":
            if aString[i-3] == "b" or aString[i+3] == "b":
                return "true"
    return "false"
