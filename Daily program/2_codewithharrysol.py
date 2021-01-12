
def LoopMusic(musicFile, stopInpt, msg):
    """
    This is the function which I will use to play the music
    """
    from pygame import mixer
    mixer.init()
    mixer.music.load(musicFile)
    mixer.music.play()
    print(msg)

    while True:
        stp = input().capitalize()

        if stp == stopInpt:
            mixer.music.stop()
            break
        else:
            print('Your input was wrong!')


def Log_Now(msg):
    """
    This is the function which I will use to log the msgs along with a time stamp
    """
    from datetime import datetime
    with open('Report.txt', 'a') as rpt:
        rpt.write(f'{msg} {datetime.now()}\n')


def MainExec(waterTm, eyesTm, exerTm):
    """
    This is function responsible for the execution of the code
    """
    from time import time
    water_init = time()
    eyes_init = time()
    exer_init = time()

    waterTm = waterTm * 60
    eyesTm = eyesTm * 60
    exerTm = exerTm * 60

    while True:
        if time() - water_init > waterTm:
            LoopMusic('The Water Song.mp3', 'Drank',
                      'Drinking water time, enter (Drank) to stop the music:')
            Log_Now('Drank Water at')
            water_init = time()
        if time() - eyes_init > eyesTm:
            LoopMusic('Eye Song.mp3', 'Eye done',
                      'Eye exercise time, enter (Eye done) to stop the music:')
            Log_Now('Eye exercise done at')
            eyes_init = time()
        if time() - exer_init > exerTm:
            LoopMusic('The Water Song.mp3', 'Exercise done',
                      'Physical exercise time enter (Exercise done) to stop the music:')
            Log_Now('Physical exercise done at')
            exer_init = time()


# Execution

# LoopMusic('The Water Song.mp3', 'Drank',
#           'Drinking time type "Drank" to stop the music')

MainExec(1, 2, 3)
