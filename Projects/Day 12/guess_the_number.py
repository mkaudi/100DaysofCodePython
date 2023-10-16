import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. type 'easy' or 'hard': ").lower()

nr_attempts = 0

if difficulty == "easy":
  nr_attempts = 10
elif difficulty == "hard":
  nr_attempts = 5

number = random.randint(0,101)

while nr_attempts != 0:
  guess = int(input(f"You have {nr_attempts} attempts remaining to guess the number. \nMake a guess: "))
  if guess == number:
    print("You guessed right, you win")
    nr_attempts = 0
  elif guess < number:
    print("Too low. \nGuess again")
    nr_attempts -= 1
  elif guess > number:
    print("Too high. \nGuess again")
    nr_attempts -= 1

if nr_attempts == 0:
  print("you've ran out of guesses, you lose.")
  print(f"The number was: {number}")

close = input("Press any button to close")






