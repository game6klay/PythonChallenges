alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z', 'a']


def SimpleSymbols(str):
    for i in str:
        if len(str) > 0:
            if i in alphabets:
                if str[i - 1] and str[i + 1] == '+':
                    str == "true"

        else:
            str == "false"
            # code goes here
    return str



#another solution could be

def SimpleSymbols(str):
    # pad the strings so that if a character exists at the beginning
    # of the string for example, we don't get on out-of-bounds error by
    # trying to get the character before it
    str = '=' + str + '='

    # loop through the entire string
    for i in range(0, len(str)):

        # check to see if current character is an alphabetic character
        if str[i].isalpha():

            # check to see if a + symbol is to the left and right
            # if not, then we know this string is not valid
            if str[i - 1] != '+' or str[i + 1] != '+':
                return 'false'

    return 'true'


