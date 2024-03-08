# week 9 , class notes 
# topic = classes, def, exceptions 

class Time:
    # class that repsresents a time of day
    def __init__(self):
        self.hours = 0
        self.minutes = 0 

    def print_time(self):
        print('Hours:', self.hours , end=' ')
        print('Minutes: ', self.minutes)
    
    def set_minutes(self, minutes):
        self.minutes = minutes
    def set_hours(self, hours):
        self.hours = hours 

my_time = Time()
print(f'{my_time.hours}hours', end=' ')
print(f'and{my_time.minutes} minutes')

my_time.hours = 7
my_time.minutes = 15
print(f'{my_time.hours}hours', end=' ')
print(f'and{my_time.minutes} minutes')

my_time = Time ()
my_time.set_hours(7)
my_time.set_minutes(15)
my_time.print_time()


# 10- 1

user_input = ''
while user_input != 'q':
    weight = int(input("Enter weight (in pounds): "))
    height = int(input("Enter height (in inches): "))

    bmi = (float(weight) / float(height * height)) * 703
    print(f'BMI: {bmi}')
    print('(CDC: 18.6-24.9 normal)\n')
    # Source www.cdc.gov

    user_input = input("Enter any key ('q' to quit): ")

user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print(f'BMI: {bmi}')
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except:
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")

# 10.3 RAISING EXCEPTIONS 

user_input = ''
while user_input != 'q':
    weight = int(input('Enter weight (in pounds): '))
    if weight < 0:
        print('Invalid weight.')
    else:
        height = int(input('Enter height (in inches): '))
        if height <= 0:
            print('Invalid height')
        
    if (weight < 0) or (height <= 0):
        print('Cannot compute info.')
    else:
        bmi = (float(weight) / float(height * height)) * 703
        print(f'BMI: {bmi}')
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
        
    user_input = input("Enter any key ('q' to quit): ")

user_input = ''
while user_input != 'q':
    try:
        weight = int(input('Enter weight (in pounds): '))
        if weight < 0:
            raise ValueError('Invalid weight.')

        height = int(input('Enter height (in inches): '))
        if height <= 0:
            raise ValueError('Invalid height.')

        bmi = (float(weight) * 703) / (float(height * height))
        print(f'BMI: {bmi}')
        print('(CDC: 18.6-24.9 normal)\n')
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")

# Week 9 class exercises 


#'''1. Create a Student class. The class should have an init function and
#member variables: first_name, last_name, id, courses. Courses should be
#a dictionary that maps a course id to a list containing course name,
#grade as percentage float, and grade as string letter (i.e. B+).
#Percentage float should be rounded to 2 decimal places.'''

#'''2. Write a member function of the class that prints all of the
#information out.'''

#'''3. Write another member function that prompts in user data for
#another course. The user should be prompted for the course id,
#course name, grade as percentage (to 2 decimal places) and grade
#as a string letter.'''

#'''a) Add exception handling to #3. Ensure that grade should be
#percentage float by using try/except. Raise a value error if
#the percentage is not between 0.00 and 100.00 (inclusive).'''


#1
class Student:
    def __init__(self, first_name,last_name,id_,courses):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id_
        self.courses = courses
#2
    def print_student_info(self):
        print("First Name: ", self.first_name)
        print("Last Name: ", self.last_name)
        print("Student id: ", self.id)
        print("Courses: ")
        for course in self.courses:
            print("Course ID: ", course)
            print("Course Name/Grade: ", self.courses[course])

#3
    def add_course(self):
        course_id = int(input("Please enter course id: "))
        course_name = input("Please enter the course name: ")
        try:
            percent = float (input("Please add a grade as a percent: "))
        except:
            print("You did not enter a floating point percentage")
        if percent < 0.0 or percent > 100.0 :
            raise ValueError("Percent out of range")
        letter = input("Please enter grade as letter: ")
        self.courses[course_id] = [ course_name, percent, letter]


student = Student("John", "Smith", 1, { 12345 : ["CIS 40", 87.5, "B+"] })
student2 = Student("Jane", "Doe", 2, { 12345 : ["CIS 40", 92.0, "A-"] })

student.print_student_info()

print()

student.add_course()
print()

student2.print_student_info()

# learn about getter and setter functions 
 # getter and setter functions - not required in the class exercises
#   def set_id(self, id_):
#       self.id = id_

#   def get_id(self):
#       return self.id

#   def set_first_name(self, first):
#       self.first_name = first

#   def get_first_name(self):
#       return self.first_name

#   def set_last_name(self, last):
#       self.last_name = last

#   def get_last_name(self):
#       return self.last_name


# there wont be any hard class questions at final 