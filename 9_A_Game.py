# The game name is Snake, water amd gun
# It is almost like rock paper scissor

import random as rd
# Given

# Defining
plrItem = ''
computerItem = ''

plrWins = []
comptWins = []


def MainGame(item1='', item2='', item3=''):
    '''
    This is the main game it can work with any itmes just
    params are of 3 items:
    ** means that first item will win over second item
    It is defined that 1 ** 2, 2 ** 3, 3 ** 1
    '''

    computerItem = rd.choice([item1, item2, item3])

    plrInput = int(input(
        f'Enter your object number: Objects are {item1}(1), {item2}(2), {item3}(3) \n'))

    if plrInput == 1:
        plrItem = item1
    elif plrInput == 2:
        plrItem = item2
    elif plrInput == 3:
        plrItem = item3
    else:
        print('Sorry you have input wrong number')
        plrItem = ''
        pass

    if plrItem == item1 and computerItem == item2:

        print('Your input is', plrItem, 'Computer input is', computerItem)
        print('You won!')
        plrWins.append(1)
        print('-----------------------------------------------')
    elif plrItem == item2 and computerItem == item3:

        print('Your input is', plrItem, 'Computer input is', computerItem)
        print('You won!')
        plrWins.append(1)
        print('-----------------------------------------------')
    elif plrItem == item3 and computerItem == item1:

        print('Your input is', plrItem, 'Computer input is', computerItem)
        print('You won!')
        plrWins.append(1)
        print('-----------------------------------------------')
    elif plrItem == computerItem:

        print('Your input is', plrItem, 'Computer input is', computerItem)
        print('It is a draw!')
        print('-----------------------------------------------')
    else:

        print('Your input is', plrItem, 'Computer input is', computerItem)
        print('Sorry you lost')
        comptWins.append(1)
        print('-----------------------------------------------')


def FinalWinner():
    '''
    This function is used to determmine who the winner is
    or is it a draw
    '''
    print('Your wins: ', plrWins)
    print('Computer wins', comptWins)
    print('-----------------------------------------------')

    if len(plrWins) > len(comptWins):
        print('YOU WON!')

    elif len(plrWins) < len(comptWins):
        print('SORRY YOU LOST!')

    elif len(plrWins) == len(comptWins):
        print('IT IS DRAW!')

    pass


# Execution
if __name__ == "__main__":
    print('')
    trys = int(input("How trys would you like: "))
    print('-----------------------------------------------')

    plrWins = []
    comptWins = []

    restart = False
    while True:
        restart = True

        while restart != False:
            MainGame('Rock', 'Paper', 'Scissor')
            break

        trys -= 1
        if trys == 0:
            restart = False
            FinalWinner()
            break
        pass
