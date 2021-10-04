"""
  Overview>

"""

# @ Imports
import Speaker
import Notification
from time import localtime
from datetime import datetime

# * Defining


def Greet(name="Master"):
    """
    """
    # Finding the correct greeting
    time_period = "morning" if localtime().tm_hour < 12 and localtime(
    ).tm_hour > 0 else "afternoon" if localtime().tm_hour < 18 and localtime().tm_hour > 12 else "evening"

    # number_rep = lambda number:"st" if number[:-1] == 1 else "nd"

    # Formulating the greeting
    greeting = f"Good {time_period}, {name}. Today is {datetime.today().date()}, and time is {datetime.today().time().hour} hours."

    Speaker.Speak(greeting)
    Notification.Notify(
        f"Today is {datetime.today().date()}, and time is {datetime.today().time().hour} hours.")



# ? Implementation
if __name__ == "__main__":
    pass
    # Speaker.Speak("Hi!")
    # Notification.Notify("Hello World!")

    Greet("Master")
