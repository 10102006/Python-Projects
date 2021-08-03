"""
  Overview

This python file will extract all the emails present in the finding text file and store it in the log file
"""

# @ Imports
import re
import os
from datetime import datetime


program_dir = "F:\\Coding & Bowsers\\Python Codes\Projects\\Email Finder"
os.chdir(program_dir)

with open("Finding Text", "r") as find:
    finding_string = find.read()

# * Defining
finding_string_compiled = re.compile(r'[a-zA-Z]+[0-9]*(@[a-zA-Z]+\.(com|net))')

emails = finding_string_compiled.finditer(finding_string)


def EnterEmail(email):
    """This function will store the email given to it in the file"""
    with open("log.txt", "a") as log:
        log.write("- " + email + "\n")


# ? Implementation
if __name__ == "__main__":
    with open("log.txt", "a") as log:
        log.write("\n")
        log.write(str(datetime.today()))
        log.write("\n")

    [EnterEmail(email.group()) for email in emails]
