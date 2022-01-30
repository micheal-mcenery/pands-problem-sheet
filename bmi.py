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

# References Week 2
# •	https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html#:~:text=How%20is%20BMI%20calculated%3F,-BMI%20is%20calculated&text=With%20the%20metric%20system%2C%20the,by%20height%20in%20meters%20squared.&text=Calculate%20BMI%20by%20dividing%20weight,a%20conversion%20factor%20of%20703
# •	https://pythonguides.com/python-print-2-decimal-places/

