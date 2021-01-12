from playsound import playsound
import time
from datetime import datetime

# thingsToDo = []
water = 4

'''
def CurrentHour():
    hr = datetime.now()
    return hr.hour


def CheckIfTime(startTime, endTime, shouldTellDiff=False,  shouldTellFalse=True):
    """
    This is the function used to check if we are between the time specified and return
    true if between the time specified
    false if not
    """
    currentHour = CurrentHour()

    if shouldTellDiff == True:
        return endTime - startTime

    if shouldTellFalse:

        if startTime < 0 or endTime > 23 or startTime > 23 or endTime < 0:
            print('Wrong time bro!')
            return False
        elif currentHour > startTime and currentHour < endTime:
            return True
        else:
            print(f' Sorry the time is: {CurrentHour()} hrs')
            return False


def Timer(minutes):
    """
    A simple timer which will return true when the time is done
    """
    waitTime = minutes * 60
    time.sleep(waitTime)
    return True


def SoundToPlay(num):
    """
    This will w b eused ot play the sounds using the parameter as a num an then using it
    """
    if num == 1:
        playsound('The Water Song.mp3')
    elif num == 2:
        playsound('Eye Song.mp3')
    # elif num == 3:
    #     playsound('The Water Song.mp3')


def WriteInTheFile(WhatToAdd):
    """
    This function will just make atime stamp of all the things done
    """

    with open('Report.txt', 'a') as report:
        report.write(f'\nYou {WhatToAdd} at {datetime.now().hour} hrs {datetime.now().min} \n')
    pass


def Main(StrtTime, EndTime, WaterAmt=2, DurationForExercise=1, DurationForEye=20):
    """
    This is the function responsble for executing the functions this is a loop
    """
    waterAmt = WaterAmt * 1000 / CheckIfTime(StrtTime, EndTime, True)
#     print(f'{CheckIfTime(StrtTime, EndTime, True)} / {WaterAmt} = {waterAmt}')

    while CheckIfTime(StrtTime, EndTime, True):

        if Timer(DurationForEye):
            SoundToPlay(2)
            print('Do eye exercise for 5 minutes')

        if Timer(30):
            SoundToPlay(1)
            print(f'Drink {waterAmt/2}ml of water or one glass of water')

        if Timer(DurationForExercise):
            print('Time To exercise')
            print('Do exercise for 10 minutes')

    print('Your work is ended Good luck, for tomorrow!')


# Execution the program
# WriteInTheFile('Drank Water')
# print('Wrote in the files')
# Main(8, 16)
'''
