from math import floor


def findPivot(list):
    length = len(list)
    startIndex = 0
    #if( list[startIndex] == list[length - 1]):
    #    startIndex = startIndex + 1
    endIndex = length - 1

    while (list[startIndex] >= list[endIndex]):
        middleIndex = floor(startIndex + ((endIndex - startIndex) / 2))
        if list[middleIndex] >= list[endIndex]:
            startIndex = middleIndex + 1
        else:
            endIndex = middleIndex

    return startIndex


def searchElementIndex(list, element):
    pivot = findPivot(list)
    #print(pivot)

    if element <= list[len(list) - 1]:
        if element == list[len(list) - 1]:
            return len(list) - 1
        else:
            binarySearchResult = binarySearch(list[pivot:], element)
            if binarySearchResult == -1 :
                return -1
            return pivot + binarySearchResult
    else:
        if element == list[0]:
            return 0
        else:
            return binarySearch(list[:pivot], element)


def binarySearch(list, element):
    if len(list) == 0:
        return -1

    mid = floor(len(list) / 2)
    if element == list[mid]:
        return mid
    else:
        if element < list[mid]:
            return binarySearch(list[:mid], element)
        else:
            binarySearchResult = binarySearch(list[mid + 1:],element)
            if binarySearchResult == -1 :
                return -1
            else:
                return mid + binarySearch(list[mid + 1:], element) + 1


#print (searchElementIndex([4,4,4,4,4,4,4,3,4],3))
#print (binarySearch([4,4,4,4,4,4,4,3,4],3))
print (searchElementIndex([4,4,5,6,7,0,1,2,3],4))