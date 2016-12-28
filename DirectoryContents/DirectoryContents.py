def printDirectoryContents(sPath):
    import os
    for child in os.listdir(sPath):
        childPath = os.path.join(sPath, child)
        if os.path.isdir(sPath,child):
            printDirectoryContents(childPath)
        else:
            print(childPath)

