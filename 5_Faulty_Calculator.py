'''
       #Summary goes here

Use:
      This will work as a normal calculator with + - * / 
      But some question will be answered wrong

*** Except for these numbers ***
     45 * 3 = 555
     56 + 9 = 77
     56 / 6 = 4r

Tasks:
      1. We will first check what operation to use
      2. If there is error then this will be skipped
      3. Then this will take two input from the user(num1 num2)
      4. Then we will check if we the error numbers are inputed
      5. If not then the normal calculation will be performed

'''

operator = input("Enter your operator please: ")

# * Divition
if operator == "/":
    print("Using divide")
    print("***********************")

  # @ Inputs
    print("Enter your first number:")
    num1 = int(input())

    print("Enter your second number:")
    num2 = int(input())

  # ? Checking if the numbers are of the error
    if num1 == 56:
        if num2 == 6:
            print("Your answer is 4")
            print("***********************")
  # ? If the number are not error numbers
    else:
        print("Your answer is\t", num1 / num2)
        print("***********************")

# * Multiplication
elif operator == "*":
    print("using multiplication")
    # Multiplication
    print("using divide")

    print("***********************")

    print("Enter your first number:")
    num1 = int(input())

    print("Enter your second number:")
    num2 = int(input())

    if num1 == 45:
        if num2 == 3:
            print("Your answer is 555")
            print("***********************")
    else:
        print("Your answer is\t", num1 * num2)
        print("***********************")

# * Addition
elif operator == "+":
    # Calculator
    print("using addtion")
    print("using divide")

    print("***********************")

    print("Enter your first number:")
    num1 = int(input())

    print("Enter your second number:")
    num2 = int(input())

    if num1 == 56:
        if num2 == 9:
            print("Your answer is 77")
            print("***********************")
    else:
        print("Your answer is\t", num1 + num2)
        print("***********************")

# * Subtraction
elif operator == "-":
    # Calculator
    print("using subtraction")
    print("using divide")

    print("***********************")

    print("Enter your first number:")
    num1 = int(input())

    print("Enter your second number:")
    num2 = int(input())

    print("Your answer is\t", num1 - num2)
    print("***********************")

# ! This is the ERROR else
else:
    # Error
    print("Wrong Input")
