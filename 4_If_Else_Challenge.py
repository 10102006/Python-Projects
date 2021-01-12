'''
       #Summary goes here

Use:
      In this we will use if, eilf and else to check if age is suitable

Tasks done:
      1. We first initialise the age required(18)
      2. This will ask the age of first to get the age
      3. Checking:
            1. if => This will check if the age is less
            2. elif => This will check if the age is 18
            3. else => This will return elgible if nothing is met

'''


print("If want to check for driver lisence then press enter")
input()

# ? Initialising the age required
requiredAge = 18

# ? Asking what age is yours
print("Enter your age:")
age = int(input())

# ! Checking
if age < requiredAge:
    print("Sorry you are not Elegible!")
elif age == requiredAge:
    print("We will not decide not come we have to meet you physicaly.")
else:
    print("You are elegible!")

# * End Statement
print("Thank you!")
