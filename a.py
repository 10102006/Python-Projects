import re


def Choose_From_List(list_object):
    """
    This function will be used to choose an item from the {list_object} in the console
        1. Printing all the items with decoration for reference
        2. Taking the input from the user of which item to choose with its index
        3. Returning the item asked => string
    """
    [print(f"{index}. {item}") for index, item in enumerate(list_object, 1)]

    item_wanted = input("Enter the index number of the item you want: ")

    if len(item_wanted) and item_wanted.isnumeric():
        item_wanted = int(item_wanted) - 1
        return list_object[item_wanted]

    elif item_wanted == '.':
        return "."

    else:
        slt_lst = re.findall("[0-9][0-9]|[0-9]", item_wanted)
        slt_lst = [int(item) - 1 for item in slt_lst]

        print(slt_lst)
        return slt_lst

    print('-----------------------------------------')
