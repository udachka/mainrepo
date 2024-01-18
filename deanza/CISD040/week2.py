##import math
##
##print('Default output of Pi:',  math.pi)
##print('Pi reduced to 4 digits after the decimal:', end=' ')
##print(f'{math.pi:.4f}') # round a floating point number to certain number amount digits

# num1= float(input("please enter a floating point number"))
# num2= float(input("please enter a floating point number"))
# print("The sum of the numbers is", num1+num2)

'''Prompt the user to read in a yearly salary. Assuming there are 52 weeks in a year, 5 days in a work week.
and 8 work hours in a day
print out the weekly,daily, and hourly salary.'''

yearly_salary= int(input("Please enter a yearly salary"))
weekly_salary= yearly_salary / 52
daily_salary= weekly_salary / 5
hourly_salary= daily_salary / 8

print("The weekly salary is", weekly_salary)
print("The daily salary is", daily_salary)
print("The hourly salary is", hourly_salary)

# Repeat problem 1 but round the amounts up to the nearest dollar
import math
yearly_salary= int(input("Please enter a yearly salary"))
weekly_salary=math.ceil( yearly_salary / 52)
daily_salary= math.ceil(weekly_salary / 5)
hourly_salary= math.ceil(daily_salary / 8)

print("The weekly salary is", weekly_salary)
print("The daily salary is", daily_salary)
print("The hourly salary is", hourly_salary)

# 3. Ask the users to give the two non-hypotenuse sides of a right triangle. 
#Using the formula a^2 + b^2 = c^2, calculate and print out the hypotenuse c of that triangle.
a = float (input("Please enter the side of a right triangle"))
b = float (input("Please enter another side of a right triangle"))

# c = sqrt ( a^2 + b^2)
c= math.sqrt(a**2 + b**2)
print("The hypotenuse is", c)

#4. The users enters in a date with the format MMDDYYYY. 
#Use modulo to break apart the three components of the date (MM, DD, and YYYY) and
# print it out in this format: MM - DD - YYYY. For example, the input might be 10042023, and the output should be 10 - 04 - 2023.
date = int(input("Please enter the date in the format MMDDYYYY: "))

month = date // 1000000 # when you want to isolate the digits
print(month)

day = (date // 10000) % 100
print(day)

year = date % 10000
print(year)

print("The date is ", month, "-", day, "-", year)

#Create a random number between 0 and 1000 (inclusive). Prompt the user for an integer also in that range.
#Print out the positive difference between the two numbers (meaning, it doesn't matter which number is bigger).
import random
num = random.randint(0, 1000)
user_num = int(input("Please enter a number between 0 and 1000: "))

print("num is", num)
print("user_num is", user_num)

print("The difference between the two numbers is", math.fabs(num - user_num))
