# first week after midterm

import math

# 1. Write a function that calculates the diameter of a
# circle given the circle's area.

def calc_diameter(are):
    # a = pi * r * r
    # d = 2 * r
    # r * r = a / pi
    # r = sqrt ( a / pi)
    # d = 2 * sqrt ( a/ pi)
    return 2 * math.sqrt (area/math.pi)
area = 10
print("Given an area of", area, "the diameter of the circle is", calc_diameter(area))


# 2. Create a function that asks student for first and
#last name (separately), student ID, classes that get read
# into a list, and expected graduation year. Create another function
# that prints out the information in this order:

# Student name:

# Student ID:

# Classes:

# Graduation Year:

def print_student_info ( first, last, student_id, classes, grad_year)
    print(first)
    print(last)
    print(student_id)
    for c in classes:
        print(c)
    print(grad_year)

def get_student_info() :
    first = input("What is your first name?")
    last = input("What is your last name?")
    student_id = input("What is your id?")
    c = ' '
    class_list = []
    while c != 'q':
        c = input("What is your class?")
        class_list.append(c)
    grad_year = input("What is your graduation year?")
print_student_info(first_name, last_name, student_id, classes, grad_year)

# 3. Prompt the user for a list of numbers. Create a function
# that takes the list in and returns a 2-element list back with
# a sum of the odd numbers in the input list and a sum
# of the even numbers in the input list.

def odd_and_even_sums (num_list):
    odd_sum = 0 
    even_sum = 0
    
    for num in num_list :
        if num % 2 == 0:
            even_sum += num
        elif num % 2 == 1:
            odd_sum += num
    return [odd_sum, even_sum]

ans = ''
num_list = []
while ans != 'q':
    ans = input("Enter a number , enter 'q' to quit")
    if ans != 'q':
        num_list.append(int(ans))

sums = odd_and_even_sums(num_list)
# look print("The odd sum is", sums[0] ## )