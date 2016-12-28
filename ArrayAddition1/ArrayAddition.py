def ArrayAddition1(arr):
    from itertools import combinations
    max_of_arr = max(arr)
    arr.pop(arr.index(max_of_arr))
    for i in range(1, len(arr) + 1):
        for lst in combinations(arr, i):
            if max_of_arr == sum(lst):
                return "true"
    return "false"