'''
       #Summary goes here

Use:
      This will get the defination of the words from the dictinary
      Then that defination will be printed

'''

# ? This is the dicinary will contain all the defination
dictinary = {
    "Ordinary": "Something that is I dunno",
    "Best Youtube": "Dani",
    "Milk": "Best Beverage",
    "Best": "Something that is best"
}

# ? This statement will ask what defination to we have to search for
print("What do you want to search :")
value = input().capitalize()

# ? This will get the defination of the we asked for
print(dictinary.get(value))
