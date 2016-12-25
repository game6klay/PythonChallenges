def AlphabetSoup(str):
    list = []

    for i in str:
        list.append(i)

    list.sort()
    new_str = ''.join(list)

    # code goes here
    return new_str


# keep this function call here


# other solution can also given as

def AlphabetSoup(strng):

	ary = list(strng)
	ary.sort()
	return ''.join(ary)

def main():

	result = AlphabetSoup("hooplah")
	

if __name__ == "__main__":
  main()