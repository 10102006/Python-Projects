"""
  Overview>

"""

# @ Imports

# * Defining

def ckeckList(lst): 
	ele = lst[0] 
	chk = True
	
	# * Comparing each element with first item 
	for item in lst: 
		if ele != item: 
			chk = False
			break; 
			
	return chk

def Common_Strings(list_string):
    """
    What to do:
        1. Comparing the string with its forward index
        2. Comparing
            1. Looping through the two list with zip
            2. If the char are equal then we will be continuing
            3. Else breaking the loop
            4. We will store all the char in a list
        3. 
    """
    newlist = [list(string) for string in list_string]
    compared = []
    for index, lst in enumerate(newlist, 1):
        if index < len(newlist):
            string = ''
            for lst1, lst2 in zip(lst, newlist[index]):
                if lst1 == lst2: string += lst1
                else: break

            compared.append(string)

    if ckeckList(compared): return (compared[0])
    elif compared[0] == '':
        print("Similarities not found")
    else:
        Common_Strings(compared)


# ? Implementation
if __name__ == "__main__":
    lst = ['Udit is a good boy', 'dit-genius', 'UditBuffaloface', 'Udit damned human']
    cp = Common_Strings(lst)
    print(cp)
