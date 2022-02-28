# squareroot.py
# This program takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Micheal McEnery


# This line defines a function which estimates the approximate square root of a positive number using Newton's Method (Reference #1)
def sqrt(x):

    tolerance = 0.000001
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
    return estimate

# This line records the user inputted positive number.
x = float(input("Please enter a positive number: "))

# This line calls the defined function to calculate the approximate square root of the user input.
sqroot = round(sqrt(x), 1)

# This line prints the output.
print("The square root of", x, "is approx.", sqroot, ".")

# References
# Reference #1: https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots