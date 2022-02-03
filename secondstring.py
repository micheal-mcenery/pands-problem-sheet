# secondstring.py
# This program asks a user to input a string and outputs every second letter in reverse order.
# Author: Micheal McEnery


# This line asks the user to enter a sentence and then reverses the input using a slice that starts at the end of the string and ends at position 0 by moving one step backwards through the input. (see reference 1 for week 3)
userInput = input("Please enter a sentence: ")[::-1]

# This line uses a slice to move two steps forward through the reversed string input, thus selecting only every second character to be printed. (see reference 2 for week 3)
print(userInput[::2])



# References
# Reference 1: https://www.w3schools.com/python/python_howto_reverse_string.asp
# Reference 2: https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python/20847220