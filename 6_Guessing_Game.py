
#  Make a number to guess
#  Take Input from plr
#  If lesser than number then the tell the player vise-virsa
#  Make a certain number of guesses
#  Type each time how many guess left
#  If number is guessed correctly then congrt and tell number of guess taken

# @ Imports
import random

# @ Variables

# * Initialising random number as the main number
playerNumber = random.randint(0, 100)

# * Number of guesses we can take
maximumNumberOfGuesses = 4

# * This will initialise the cuurtguess to maxguess so that we can decrease then each turn
CurrentNumberOfGuesses = maximumNumberOfGuesses

if __name__ == "__main__":
    print('To start the game press enter')
    enter = input()

  # ! Directions to the player
    print('\t*Instructions*')
    print('You have to guess a number between 100 and 0', end=" ")
    enter = input()
    print('We will tell you if number is greater or less', end=" ")
    enter = input()
    print('You have', maximumNumberOfGuesses + 1, 'Trys', end=" ")
    enter = input()
    print('Have Fun!', end=" ")
    enter = input()

  # ? First Try
    guess = int(input('Your number please: '))
    print('\tYou have', CurrentNumberOfGuesses, 'Guesses left')

  # * Other trys
    while guess != playerNumber:
        if CurrentNumberOfGuesses > 0:

            # Greater Lesser mechanic
            if guess < playerNumber:
                print('Your number is Less than desired number')
            elif guess > playerNumber:
                print('Your number is Greater than desired number')

            # Retry Mechanic
            print('')
            guess = int(input('Try again: '))
            CurrentNumberOfGuesses = CurrentNumberOfGuesses - 1
            print('\tYou have', CurrentNumberOfGuesses, 'Guesses left')

        else:
            # Lose mechanic
            print('')
            print('Sorry you have lost missed all your Trys!')
            print(f"The Correct number is {playerNumber}")
            break

  # * Winning mechanc
    if guess == playerNumber:
        print('')
        print('Your answer is correct :)')
        print('You have completed in',
              (maximumNumberOfGuesses - CurrentNumberOfGuesses) + 1, 'Guesses')
