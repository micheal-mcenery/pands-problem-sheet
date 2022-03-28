# es.py
# # program that reads in a text file and outputs the number of e's it contains
# Author: Micheal McEnery


# These lines imports the Python "sys" module which provides access to command-line arguements via sys.argv, in which I indicate argument "1" on the command-line as the source of the filename (Reference #1)
import sys
filename = sys.argv[1]


# This line creates a variable called "counter" which will be used to track the number of "e" or "E" which occur.
counter = 0


# The below line will prompt this program to try to open the file specified in arguement "1" on the command-line. (Reference #3)
try:
    # These lines open the file specified in argument "1" on the command-line in reading mode, read each line of the text, check whether each character on a line is an "e" or "E", and if so, add +1 to the counter, and lastly, prints the final counter. (Reference #2)
    with open(filename, 'r') as f:
        for line in f:
            for character in line:
                if character == "E" or character == "e":
                    counter += 1
    print(counter)
# However, if the file name or path is incorrect, the following statement will be printed.
except FileNotFoundError:
    print("No such file. Check file name and path and try again.")


# References:
# Reference #1: https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# Reference #2: https://www.pythontutorial.net/python-basics/python-read-text-file/
# Reference #3: https://codereview.stackexchange.com/questions/83241/user-input-function-keep-looping-until-valid-filename-entered