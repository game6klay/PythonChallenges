def isPalindrome(str):

    reversed_str = str[::-1]
    return "true" if (str == reversed_str) else "false"

def Palindrome(str1):

    cmp_str = str1.replace(" ","") #remove the place if there are any spaces in between

    return "true" if (cmp_str == cmp_str[::-1]) else "false"