# A.
# Feyza Atabey 
# Lab 6 : creating a file response.txt 

# B. - Write a few sentences about how you hope to use what you've learned in this class in the future. You can write
#whatever you'd like, but make sure your response is at least 3 sentences long to have enough text. Store your response
#in a variable and write it out to a file called response.txt.
import string
from collections import Counter

response_text= """I am excited to apply the programming skills I've learned in this class to solve problems. 
By automating tasks with python, I can save time  and gain hands on experience.
Furthermore, I look forward to turn this satisfying problem solving knowledge into a career one day. """

with open('response.txt', 'w') as file:
    file.write(response_text)

#- Prompt the user to search for a word to see how many times it occurred in the text
search_word= input("Enter a word to search for: ").lower()

#- Read in the text from the file back into a variable
with open('response.txt','r') as file:
    text = file.read()

#- Create a dictionary of how many times each word occurred, with words being separated by space. 
'''#For instance, your dictionary might start like this with the first word: {'I' : 1}. Only alphanumeric characters should be considered; please
#remove all punctuation marks (i.e. if there's a comma at the end of the word, it should not be considered a different
#word). Numbers can be considered as words if they're stand-alone (i.e. "20"). Capitalization should not matter, so a
#word like "If" and "if" should be considered the same.'''

def count_words(text):
    text = text.translate(str.maketrans('','',string.punctuation)).lower()
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
word_counts = count_words(text)
# Append to the response.txt file out how many times the user's word occurred in the text.
with open('response.txt', 'a') as file:
    file.write(f"\nThe word '{search_word}' occured {word_counts.get(search_word, 0)} times. \n")

#- Append to the response.txt file the top 5 most common words in your response along with the word counts.

word_counts_counter = Counter(word_counts)
top_5_words = word_counts_counter.most_common(5)

with open ('response.txt', 'a') as file:
    file.write("The top 5 most common  words: \n")
    for word,count in top_5_words:
        file.write(f"'{word}' : {count}\n")

