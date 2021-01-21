"""
  Overview

What is done:
    1. CheckList:
        ** This function will check if all the items the given list are same or not
    2. Common_String:
        ** Main function this will return the common attribute in two or more string which must be passed by a list
        ** This will also check if there are any common attributes or not

"""

# @ Imports

# * Defining


def CheckList(lst):
    """
      What is done:
        1. Obtaining the first element of the list for comparision
        2. check is the variable which we will return, it will True by default
        3. Then looping through
        
    """
    first_element = lst[0] 
    check = True
	
	# * Comparing each element with first item
    for item in lst: 
        if first_element != item: 
            check = False
            break; 
    return check


def Common_Strings(list_string):
    """
    What to do:
        1. Comparing the string with its forward index
        2. Comparing
            1. Looping through the two list with zip
            2. If the char are equal then we will be continuing
            3. Else breaking the loop
            4. We will store all the char in a list
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

    if CheckList(compared): return (compared[0])
    elif compared[0] == '':
        print("Similarities not found")
    else:
        Common_Strings(compared)


# ? Implementation
if __name__ == "__main__":
    lst = ['Udit is a good boy', 'Udit-genius', 'UditBuffaloface', 'Udit damned human']
    cp = Common_Strings(lst)
    print(cp)

