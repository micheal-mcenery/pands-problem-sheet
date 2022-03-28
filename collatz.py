# collatz.py
# A program which asks the user to input any positive integer and outputs the successive values of the following calculation:
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Author: Micheal McEnery


# This line records the user input as "p_integer" and converts it into an integer.
p_integer = int(input("Please enter a positive integer: "))

# This line stores the output which will eventually be printed below. Initailly this variable only contains the user input (converted to a string) and a space (" ").
output = str(p_integer) + " "

# This while loop will continue looping the if statement until the integer = 1.
while p_integer != 1:
    # The if statement assesses whether the positive integer is even or odd, performs the relevent calculations, and adds the result to the output variable.
    if p_integer % 2 == 0:
        p_integer = p_integer // 2
        # The below line updates the output varable, so that p_integer (following calculation) is added to the output varable, as well as a space (" ") (same on  line 22).
        output = output + str(p_integer) + " "
    else:
        p_integer = (p_integer * 3) + 1
        output = output + str(p_integer) + " "

# This line prints the output.
print(output)