
def exoh(str):
    return "true" if str.count('o') == str.count('x') else "false"

def exoh2(str2):
    return (str.count('o')== str.count('x')) and "true" or "false"


def checkOccurence(str):
    count_o =0
    count_x =0
    for i in str:
        if str[i] == 'o':
            count_o+=count_o
        elif str[i] == 'x':
            count_x+=count_x

    if (count_x == count_o):
        return "true"
    else:
        return "false"



print
checkOccurence("xoox")