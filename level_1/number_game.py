#random number
import random
num = random.randint(1, 100)

#number of guesses
guesses = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#loop until the user guesses the correct number
while True:
    guess = input("Make a guess: ")

#check if the input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    guesses += 1

#check if the guess is correct, too high, or too low
    if guess < num:
        print("Too low.")
    elif guess > num:
        print("Too high.")
    elif guess == num:
        print(f"Congratulations! You've guessed the number {num} in {guesses} attempts.")
        break
#limit the number of guesses to 10
    if guesses >= 10:
        print(f"Sorry, you've used all your attempts. The number was {num}.")
        break