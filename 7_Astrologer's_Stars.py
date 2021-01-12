'''
     Pattern printing
2. input = int n

3. boolean = take 1 0 and make it a tue or false

Yo

4. if TRUE n = rows
*****
****
***
**
*

5. if FALSE n = rows
*
**
***
****
*****
'''

# @ DEFINING


def PrintPattern(identationOfThepattern, NumberOfRows):
  # ? This will print greater to less
    if identationOfThepattern == True:
        while NumberOfRows != 0:
            print('\t', '*' * NumberOfRows)
            NumberOfRows -= 1
        print('')

  # ? This will print less to greater
    elif identationOfThepattern == False:
        nums = 0

        while nums != NumberOfRows:
            print('\t', '*' * nums)
            nums += 1
        print('')

  # ! This is for error
    else:
        print('')
        print('!Sorry You error occured!')
        print('Perhaps you might have put wrong number in the Order!\n')
        print('')


CheckOrder = lambda order: True if order == 1 else False

def Main():
    restart = False
    input('Press enter to continue: ')

    while True:
        restart = True

        print('')
        Order = int(input("In which order would you like 1 or 0\n"))
        CheckOrder(Order)
        Rows = int(input("How many rows would you like to print: "))

        while restart != False:
            PrintPattern(CheckOrder(Order), Rows)
            break

        Continue = int(input('To Continue press 1 and To Exit press 0\n'))

        if Continue == 0:
            restart = False
            break
        pass


def New_Astrologer(n_stars=int(input('Number of Stars(): '))):
    """
          * Note that this a function I have made as an improvement

          Things done:
                1. Asking how many star lines need in the param ~ I didnt knew that this could be done
                2. Initialising a list where we will add the star lines this can also be a prelist 
                3. The with short if defining t/f for the order of the pyramid
                4. Appending Stars to previous list
                  1. outside intialising an index for the space in front of the stars
                  2. Looping till the number of stars ~ 1
                  3. In each loop adding a star
                        1. This is a f-string because we need some indexing
                        2. Adding spaces respect to the index of the spacing ~ 4.1
                        3. Adding number of stars as the spacing is done with ~ 4.2
                        4. At last appending the star var in the stars squence ~ 2
                5. Printing all the stars in the star squence via looping through it

    """
    s_sequence=[]
    s_order = True if int(input(
        'Enter your input "1" for pyramid "2" for reverse : ')) == 2 else False

    i_space = n_stars

    for i_star in range(n_stars + 1):
        star = f"{' ' * i_space}{'* ' * i_star}"
        s_sequence.append(star)
        i_space -= 1

    for star in sorted(s_sequence, reverse=s_order):
        print(star)


# @ EXECUTION
if __name__ == "__main__":
    New_Astrologer()
    while True:
        if True if input('Do you want to continue(y/n): ').capitalize() == 'Y' else False:
            New_Astrologer(int(input('Number of Stars(): ')))
        else:
            break
