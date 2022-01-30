# Week 2 BMI Calculator. This file calculates a persons BMI based on weight and height input.
# Author: Micheal McEnery

# This line asks the user to input their weight (as a string) and then converts their input to an integer.
weight = int(input("Enter weight(kg): "))

# This line asks the user to input their height (as a string) and then converts their input to an integer.
height = int(input("Enter height(cm): "))

# Because height is commonly measured in centimeters, divide height in centimeters by 100 to obtain height in meters (see references for week 2).
height_in_meters = height / 100

# This line calculates BMI using the formula "weight (kg) divided by (height (m) squared)" (see references for week 2)
bmi = weight / (height_in_meters * height_in_meters)

# This line formats the BMI to two decimal places (see references for week 2)
format_bmi = "{:.2f}".format(bmi)

# This line converts BMI to a string and prints the final output.
print("Your BMI is " + str(format_bmi))