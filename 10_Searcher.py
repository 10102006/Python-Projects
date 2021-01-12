'''
    #Summary
    
This is a challenge about the coroutines!

Tasks:
      1. Make a function that will make the text list
      2. Then initialise the text into the coroutine
      3. Then in the coroutine the search will check for the input

'''

# @ Defining

NamesDictinary = {}


def MakeText():
    """
     This method will make the text at the random index with the names from the nameslist
     Then this will intialise the names and the index in the list in the dictinary
    """
  # * This is importing  random module for randomly generated numbers for names
    import random

  # * This is the list of name which will have an index
    nameslist = ['Udit', 'Yachna', 'Aryan', 'Karan', 'Deepak']

  # ! This is the main dict in which will intialise the index then we will search for them
    NamesDictinary = {}

  # * In this loop we are intialising random index
    for name in nameslist:
        index = random.randint(1, len(nameslist))
        NamesDictinary.update({name: index})
  # @ Printing that index for surity
    print(NamesDictinary)


def LoadingAnimation(textToBeShowen, numberofdots=5):
    """
          This function will animate the dots after the text is showen 
          This will be like the downloading animation but in the terminal
    """
    import time
    import sys

    for n_dots in range(numberofdots):
        sys.stdout.write(f'\r{textToBeShowen}{"." * n_dots}')
        time.sleep(0.8)

    print('')


def Search():
    """
     This method is the main coroutine that will initialise the indexes
      and also Search for the names
    """

    # ! This is the initialisation of the text
    LoadingAnimation("Initialising", 8)
    MakeText()

    # ? This is the searching coroutine
    print('Initialised!')
    while True:
        name = (yield)

        if NamesDictinary.get(name):
            print(f'Name is present and index is {NamesDictinary.get(name)}')
        else:
            print('Either name is not present or wrong input!')
        print('--------------------------------------------------------------------------------')


# ? Execution
if __name__ == '__main__':

    NameBook = Search()

    next(NameBook)

    while True:
        name = input('Which name do you want to search for: \n').capitalize()
        if name == '1':
            break
        else:
            NameBook.send(name)
