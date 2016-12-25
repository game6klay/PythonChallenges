def FirstReverse(str):
    # the easiest way to reverse a string in python is actually the following way:
    # in python you can treat the string as an array by adding [] after it and
    # the colons inside represent str[start:stop:step] where if step is a negative number
    # it'll loop through the string backwards
    return str[::-1]



def FirstReverse(str):
    # reversed(str) turns the string into an iterator object (similar to an array)
    # and reverses the order of the characters
    # then we join it with an empty string producing a final string for us
    return ''.join(reversed(str))




def reverse_a_string_slowly(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1                    # index = index - 1
        new_string += a_string[index] # new_string = new_string + character
    return new_string