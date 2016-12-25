# creating a dictionary of vowels and a list of alphabets

vowels ={'a':'A','e':'E','i':'I','o':'O','u':'U'}

alphabets = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', 'a']

dic = {}

# putting all the values of the alphabets into the respected values of the dictionary

for i in alphabets:
    dic[alphabets[i]]= alphabets[i+1]

def letterChanges(str):

    text = ""

    for i in str:
        if i in alphabets:
            i = dic[i]
            text += i

    text2 = ""

    for i in text:
        if i in vowels:
            i = vowels[i]
        text2 += i


    return text2

