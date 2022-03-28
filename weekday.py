# weekday.py
# This program outputs whether or not today is a weekday.
# Author: Micheal McEnery


#This line imports datetime.
from datetime import datetime

# This line records the day of the week as "Day" variable. Day of the week ranges from 0 (Monday) to 6 (Sunday). (Reference #1)
Day = datetime.today().weekday()

# This if statement checks if "Day" is a weekday (range of 0 - 5, or numbers 0, 1, 2, 3, and 4) or weekend day (else) and prints the aproporiate phrase (Reference #2).
if Day in range(0, 5, 1):
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the Weekend, yay!")


# References
# Reference 1: https://www.delftstack.com/howto/python/python-datetime-day-of-week/
# Reference 2: https://www.tutorialkart.com/python/python-range/python-if-in-range/#:~:text=To%20check%20if%20given%20number,in%20keyword%20as%20shown%20below.&text=number%20in%20range()%20expression,not%20to%20the%20existing%20syntax.