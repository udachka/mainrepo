# Class notes Week 10 - 2 more before final 
# Final will be in person 

"""
Python Notes: Using an Imported Module

1. Importing a Module
   - To use functionalities defined in a module, it must first be imported.
   - Syntax: import module_name

Example:
import HTTPServer

2. Accessing Module Attributes
   - Attributes (variables, functions, classes) of an imported module can be accessed using the dot (.) operator.
   - Syntax: module_name.attribute_name

Example:
my_ip = HTTPServer.address
print(f"The server address is: {my_ip}")

3. Modifying Module Attributes
   - Attributes of a module can be modified in the current Python instance. This does not change the module permanently.
   - Syntax: module_name.attribute_name = new_value

Example:
HTTPServer.address = "www.yahoo.com"
print(f"The updated server address is: {HTTPServer.address}")

Note: Such modifications are temporary and exist only during the current program execution.

4. Temporary Nature of Changes
   - Changes made to a module's attributes are not persistent across program executions. 
   - Re-importing the module in a new execution restores the original attributes.

Demonstration:
- Modify an attribute in one script.
- Check the value in a second script after the first script finishes execution.

Script 1: modify_attribute.py
-----------------------------
import HTTPServer
HTTPServer.address = "www.yahoo.com"

Script 2: check_attribute.py
----------------------------
import HTTPServer
print(f"The server address is back to: {HTTPServer.address}")

5. Step-by-Step Example
   a. Assume a module named HTTPServer.py with a defined attribute 'address'.
   b. Import the module in your script.
   c. Access the attribute using the dot operator.
   d. Modify the attribute.
   e. Restart your script or Python interpreter to see the attribute's original value.

Example Code:
-------------
# Assuming HTTPServer.py exists and has an attribute 'address'

# Step 1: Import the module
import HTTPServer

# Step 2: Access the attribute
print(f"Current address: {HTTPServer.address}")

# Step 3: Modify the attribute
HTTPServer.address = "www.yahoo.com"
print(f"Updated address: {HTTPServer.address}")

# Step 4: After restarting the interpreter or script
# This code would show the original address value
import HTTPServer
print(f"After restart, address: {HTTPServer.address}")
"""

# This is a formatted note for educational purposes and won't execute as-is due to the placeholder module and attribute names.

print('Opening file myfile.txt.')
f = open('myfile.txt')  # create file object

print('Reading file myfile.txt.')
contents = f.read()  # read file text into a string

print('Closing file myfile.txt.')
f.close()  # close the file

print('\nContents of myfile.txt:')
print(contents)

# Read file contents
print ('Reading in data....')
f = open('mydata.txt')
lines = f.readlines()
f.close()

# Iterate over each line
print('\nCalculating average....')
total = 0
for ln in lines:
    total += int(ln)

# Compute result
avg = total/len(lines)
print(f'Average value: {avg}')

"""Echo the contents of a file."""
f = open('myfile.txt')

for line in f:
    print(line, end="")

f.close()

# if you do not have a file under that name , python will create a new one.
# if you have a file under that name, it will override , it wont add up to it. 

f = open('myfile.txt', 'w')  # Open file
f.write('Example string:\n  test....')  # Write string
f.close()  # Close the file

num1 = 5
num2 = 7.5
num3 = num1 + num2

f = open('myfile.txt', 'w')
f.write(str(num1))
f.write(' + ')
f.write(str(num2))
f.write(' = ')
f.write(str(num3))
f.close()

"""
Python File Modes for open() Function:

1. 'r' Mode:
   - Description: Open the file for reading.
   - Read: Yes
   - Write: No
   - Create File if Not Exists: No
   - Overwrite Existing File: No

Example:
with open('example.txt', 'r') as file:
    contents = file.read()
    print(contents)

2. 'w' Mode:
   - Description: Open the file for writing. If the file does not exist, then the file is created. Contents of an existing file are overwritten.
   - Read: No
   - Write: Yes
   - Create File if Not Exists: Yes
   - Overwrite Existing File: Yes

Example:
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

3. 'a' Mode:
   - Description: Open the file for appending. If the file does not exist, then the file is created. Writes are added to the end of existing file contents.
   - Read: No
   - Write: Yes
   - Create File if Not Exists: Yes
   - Overwrite Existing File: No (appends instead)

Example:
with open('example.txt', 'a') as file:
    file.write('\\nNew line appended.')

Note: Always ensure to close the file after your operations are complete to free up system resources. Using the 'with' statement as shown in the examples ensures that the file is closed automatically once the block is exited.
"""
# Class exercises Week 10

'''
1. Prompt the user to write a few sentences about future academic interests.
Split the string into individual words and write them out line by line
into a file called words.txt. (Don't worry about removing punctuation
marks for this exercise)
'''
interest = input("Please write a few sentences about your future academic interests: ")
words = interest.split()
f = open('words.txt', 'w')
for word in words:
    f.write(word = '\n')
f.close()

'''
2. Read in the words from the text file line by line and calculate
the average word length. Then, print it to screen.
'''

f = open('words.txt', 'r')
words = f.readlines()
length = 0
num_words = len(words)

for word in words:
    length += len(word[:-1])
print("The average word lenght is", length/ num_words )
f.close()
