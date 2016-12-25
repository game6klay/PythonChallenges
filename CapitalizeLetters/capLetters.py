def lettersCapitalize(str):

    test = []

    for word in str.split():
        test.append(word.title())
        new_str = " ".join(test)

    return new_str