# Fibonacci sequence
# This is the sequence : 0 1 1 2 3 5 8 13 .........
# The formula is that we have to add the number behind the curr number and print that number and continue

"""
1. Take input
2. Recursive function with param as the numbers req and feed input as that
"""

# ? Defining


def i_Fibonacci(numberofsequence):
    """
      Things Done:
            1. Making a mock list with 0, 1 as basic
            2. Then using i and j as index
            3. Looping till the numbers of indexes are printed
    """
    f_sequence = [0, 1]
    i = 0
    j = 1

    for _ in range(int(numberofsequence) - 2):
        next_i = i + j
        f_sequence.append(next_i)
        i = j
        j = next_i
    for num in f_sequence:
        print(num)


# @ Execution
if __name__ == "__main__":
    num2 = int(input("Enter something: "))
    i_Fibonacci(num2)
