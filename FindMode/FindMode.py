from collections import Counter
data = Counter(list)
data.most_common()
data.most_common(1)

# using a package

from statistics import mode
mode(list)
from collections import Counter
data = Counter(list)
data.most_common() # return all the entry with its occurances
data.most_common(1) # return the entry with the highest occurance
max(set(list), key=list.count)


