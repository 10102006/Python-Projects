"""
  Overview>

This will notify the user when a function is run and also it will have some timer and stuff

"""

# @ Imports

# * Defining
from plyer import notification
# import time

# time.sleep(30)

# ? Implementation
if __name__ == "__main__":
  notification.notify(
    title='testing',
    message='message',
    app_icon=None,
    timeout=10,
  )
  print("Hello world")
