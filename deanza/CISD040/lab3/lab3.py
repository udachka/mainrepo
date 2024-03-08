# A. Feyza Atabey
# Lab 3 - Guessing Numbers between 1 and 20

import random
# B. Write a Python program (20 pts) that plays the guess-the-number game with the user.
#The program will play 5 games. In each game, the program comes up with a random target number between 1 and
#20, inclusive, and lets the user guess the target number until the user guesses correctly. With each guess the program
#prints "too high", "too low", or "you got it".
#- The program uses the random module to get a random number.
#- At the top of the .py file, import the random module so you can use it.
#- Whenever you need a random number, the format is: randNum = random.randint(a, b)
# where randNum is a random integer that is between a and b, inclusive
# 1. A getInput function that will get the user guess a number between 1 and 20.
# - The function has a loop that keeps looping as long as the input number is not between 1 and 20.
# - The condition for the loop must be whether or not the number is between 1 and 20.
#- In the loop, try to prompt the user and read in an integer
#- Return the user input number when it's valid.

def getInput() :
    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 20: "))
            if 1 <=user_guess <= 20:
                return user_guess
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Thats no a valid number. Please try again.")

# 2. A checkNum function that will check the user's guess against the target number.
# - Check the user's guess against the target number.
# - Return 1 of 3 strings: "too low", "too high", "you got it"

def checkNum (guess, target):
    if guess < target:
        return "too low"
    elif guess > target:
        return "too high"
    else:
        return "you got it"

# 3. A main function that will:
# - Loop to let the user play the game 5 times.
#In the loop:
#o Create a random number
#o Create an inner loop that continues to call getInput to ask for a guess, and checkNum to check the guess.
#The loop keeps running until checkNum returns the string "you got it".
#The condition for the inner loop must be whether the return string is "you got it".
#- Count down and print the number of games that the user still has left.
#- Don't forget to call the main function so the program will run.

def main():
    for game in range(5):
        target_number = random.randint(1,20)
        print(f"Game {game+1}. Guess the number!")

        while True:
            guess = getInput ()
            result = checkNum(guess, target_number)
            print(result)
            if result == "you got it":
                break
        print(f"Games left: {4 - game}")

if __name__ == "__main__":
    main()


