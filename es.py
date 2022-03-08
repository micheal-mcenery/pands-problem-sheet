# es.py
# # program that reads in a text file and outputs the number of e's it contains
# Author: Micheal McEnery


# These lines imports the Python "sys" module which provides access to any command-line arguements via sys.argv (Reference #1)
import sys
filename = sys.argv[1]


# This line creates a variable called "counter" which will be used to track the number of "e" or "E" which occur.
counter = 0


# These lines open the file specified on the command-line in reading mode, read each line of the text, check whether each character on a line is an "e" or "E", and if so, add +1 to the counter. (Reference #2)
with open(filename, 'r') as f:
    for line in f:
        for character in line:
            if character == "E" or character == "e":
                counter += 1


# This line prints the final counter
print(counter)


# References:
# Reference #1: https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# Reference #2: https://www.pythontutorial.net/python-basics/python-read-text-file/