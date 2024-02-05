#week3 - class exercises
my_list = [10, "test", 1.99] #3.2.4 zybook
print(my_list)

my_list.append(2)
print(my_list)

my_list.pop(1)
print(my_list)

my_list.remove(10)
print(my_list)

sample_dictionary = {'test': 20, 'test2' : 30}
sample_dictionary['test3'] = 30 
print(sample_dictionary)

#4.2.5
user_num = int(input('Enter a number: '))

div_remainder = user_num % 2

if div_remainder == 0:
    print(f'{user_num} is even.')
else:
    print(f'{user_num} is odd.')



# week 3 class exercises
    
#1. Prompt the user to enter in the name of a US City. Print out whether the length of the US City is divisible by 3. 
#If it is, then print out the first and last letters in the city name. 
#If not, just print out that the city length is not evenly divisible by 3

city = input('Please enter the name of the city')
name_length = len(city)
if name_length % 3 == 0 :
    print(city[0] + city[-1] )
else:
    print('City length is not divisible by 3')

#2. Prompt the user to enter in 5 different names. 
#Put the names into a list and then iterate through the list to figure out which one is earliest in alphabetical order.

name1 = input('Please enter a name: ')
name2 = input('Please enter a name: ')
name3 = input('Please enter a name: ')
name4 = input('Please enter a name: ')
name5 = input('Please enter a name: ')
names = [name1, name2, name3, name4, name5]

earliest = name1 
if names[1] < earliest:
    earliest = names[1]
if names[2] < earliest:
    earliest = names[2]
if names[3] < earliest:
    earliest = names[3]
if names[4] < earliest:
    earliest = names[4]
if names[5] < earliest:
    earliest = names[5]

print(earliest, "is the earliest name on the alphabet")

#3. You have the following data for low temperatures:

#San Jose: 50

#San Francisco: 55

#Los Angeles: 60

#San Diego: 65

#Sacramento: 45

#Put the data into a dictionary by creating an empty dictionary, then adding the data points in one at a time.

#Finally, delete the entry for Los Angeles.
# to create an empty dictionary we use curly {}

temps = {}
temps ['San Jose'] = 50
temps ['San Francisco'] = 55
temps ['Los Angeles'] = 60
temps ['San Diego'] = 65
temps ['Sacramento'] = 45
del temps ['Los Angeles']

# midterm !!!! branches and if statements
#4. You have a ride with the following restrictions:

#Age - must be 12 or over to ride independently, must be at least 8 to ride with a guardian

#Height - must be 54 inches to ride independently, must be 48 inches to ride with a guardian

#Prompt the user for age and height and print the user's status: can't ride, ride with guardian, or ride independently.
#Keep in mind that both conditions (age and height) must be met for a given status.

age = int(input(' Please enter your age: '))
height = int(input('Please enter your height: '))

if age < 8 or height < 48:
    print('Sorry, you cant ride ')
elif age < 12 or height < 54: 
    print('You can ride with a guardian')
else:
    print('You can ride') 