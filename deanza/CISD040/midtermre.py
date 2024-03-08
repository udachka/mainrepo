# 1. Prompt the user to enter the name of the city the user lives in.
# Print out whether the city name has an odd or even number of letters. 
# Spaces and dashes don't count as letters for this problem.

city_name = input("Please enter the name of the city you live in:  ")
count = 0
for letter in city_name :
    if letter != ' ' and letter != '-':
        count += 1
if count % 2 ==  1:
    print(city_name, "has an odd number of characters")
else :
    print(city_name, "has an even number of characters")

# 2. Prompt user to enter in integers and append them to a list until the user is finished. 
#Print out the 2nd largest number in the list.
# You may use list functions covered in 3.2 to solve the problem.

user_response = 0
num_list = []
while user_response != 'q':
    user_response = input("Please enter an integer, or q to quit. \n")
    if user_response != 'q':
        num_list.append(int(user_response))
second_max_val = min(num_list)
max_val = max(num_list)

for num in num_list:
    if num > second_max_val and num != max_val:
        second_max_val = num
print(second_max_val)

# 3. Prompt the user to enter in a 10 digit telephone number in the US format: 
#nnn-nnn-nnnn, where each n stands for a digit.
#Create a dictionary of how many times each digit appears in the number 
#and print out the final dictionary.

phone_num = input("Please enter a phone number in the format nnn-nnn-nnnn\n")
digit_counts = {'0':0,'1':0,'2':0,'3':0,'4':0, '5':0,'6': 0,'7':0,'8':0,'9':0}
for digit in phone_num:
    if digit != '-':
        digit_counts[digit] += 1
print(digit_counts)
