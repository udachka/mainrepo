# dictionary + more advanced 

#1. Prompt user for a sentence about programming. 
# Slice the string for every other character. 
#Then, count the  number of vowels and consonants 
#(punctuation and spaces don't count) and print those values out.

sentence = input ("Please enter a sentence about programming: ")
every_other = sentence [::2]

vowel_count = 0
consonant_count = 0

for ch in every_other:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        vowel_count += 1
    elif ch != ;' ' and ch != '.' and ch != '!' and ch != '?' and ch != '-' and ch != ',' and ch != '/' :
        consonant_count += 1
print(every_other, "has", vowel_count, "vowels and", consonant_count, "consonants")

#'''2. Prompt user for another sentence about programming. Then ask
#user to enter in a word. Using string methods to check if the word
#is in the sentence.'''

sentence2 = input("Please another another sentence about programming: ")
word = input("Please enter a word(no spaces): ")

if word in sentence2:
    print(word, "is in: ", sentence2)
else:
    print(word, "is not in:  ", sentence2)

#3. Use a while loop to keep prompting user for more positive integers
#until user types -1.

#a) Append these inputs to a list.

#b) Once you have a list, create a dictionary with the frequencies
#of each number in the list.

#c) Finally, iterate through the dictionary to print out the mode
#(most common number) in the list. If there are multiple modes, you can just
#print one of them
    
num = 0 
num_list = []
while num != -1 :
    num = int(input("Please enter a positive integer, -1 when finished: "))
    if num != -1:
        num_list.append(num)

#Example:
# num_list -> [1,2,1,3,1]
# freq -> {1 :3, 2 : 1, 3:1}        
freq = {}
for n in num_list:
    if n in num_list.keys():
        freq[n] += 1
    else:
        freq [n] = 1

#example:
# max_value = 1
#max_freq = 3
#  freq -> {1 :3, 2 : 1, 3:1} 
        
max_value = 0
max_freq = -1 
for number, frequency in freq.items():
    if frequency > max_freq:
        max_value = number
        max_freq = frequency
print(max_value, "is the mode with a frequency of", max_freq)
