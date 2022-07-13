#Write a Python program to calculate number of days between two dates.
from datetime import date
first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)
result = last_date - first_date
print("there are left", result.days, "days from", first_date, "until", last_date)