"""
  Overview

"""

# @ Imports
from plyer import notification

# * Defining
def NotifyMe(message):
    notification.notify(
        title = 'Desktop Assistant',
        message = message,
        app_icon = 'E:\Coding & Bowsers\Python Codes\Projects\Destop Assistant\Assistant Icon.ico',
        timeout = 10
    )

# ? Implementation
if __name__ == "__main__":
   NotifyMe(input('Enter notified: '))