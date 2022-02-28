# weekday.py
# This program outputs whether or not today is a weekday.
# Author: Micheal McEnery


#This line imports datetime.
from datetime import datetime

# This line records the day of the week as "Day" variable. Day of the week ranges from 0 (Monday) to 6 (Sunday). (Reference #1)
Day = datetime.today().weekday()

# This if statement checks if "Day" is a weekday (0 - 4) or weekend day (else) and prints the aproporiate phrase.
if Day == 0 or 1 or 2 or 3 or 4:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the Weekend, yay!")


# References
# Reference 1: https://www.delftstack.com/howto/python/python-datetime-day-of-week/