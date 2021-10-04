"""
  Overview>

This will notify the user when a function is run and also it will have some timer and stuff

"""

# @ Imports

# * Defining
from plyer import notification
import os

# import time

icon = os.path.join(os.getcwd(), "icon.ico")

# time.sleep(30)


def Notify(message):
    """
    Basic notifcation making function
    """
    notification.notify(
        title="ARIEL(1.1)",
        message=message,
        app_icon=icon,
        timeout=10
    )


# ? Implementation
if __name__ == "__main__":
    notification.notify(
        title='testing',
        message='message',
        app_icon=icon,
        timeout=10,
    )
