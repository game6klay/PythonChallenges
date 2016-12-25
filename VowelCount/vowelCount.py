def vowelCount(str):
    count = 0
    for char in str:
        if char in "aeiouAEIOU":
            count += 1
    return count
