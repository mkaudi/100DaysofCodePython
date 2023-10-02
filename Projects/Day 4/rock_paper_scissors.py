rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

rpc_option = [rock, paper, scissors]
player1 = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer = random.randint(0,2)

if player1 >2:
  print("Invalid Input! You lose")
else:
  if player1 == computer:
    print("Draw")
  else:
    print(rpc_option[player1])
    print("Computer chose:\n")
    print(rpc_option[computer])
    if player1 == 0 and computer == 1:
      print("You lose")
    elif player1 == 0 and computer == 2:
      print("You win!")
    elif player1 == 1 and computer == 0:
      print("You win!")
    elif player1 == 1 and computer == 2:
      print("You lose")
    elif player1 == 2 and computer == 0:
      print("You lose")
    elif player1 == 2 and computer == 1:
      print("You win")
    else:
      print("Invalid input! You lose")