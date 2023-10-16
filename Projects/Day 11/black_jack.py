import random
#import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

#get a card and put/append it into the card list
def draw_card(card_list):
  card = cards[random.randint(1,12)]
  card_list.append(card)
  return card_list

"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

#calculcate the score while drawing new cards
def scores(user_list, comp_list, user_score, comp_score, final):
  user_score = 0
  comp_score = 0
  #count the users cards
  for i in user_list:
    user_score += i
 
   #draw the computer's card
  draw_card(comp_list)
  
    #count the computer's cards
  for i in comp_list:
    comp_score += i
  if final == True:
    print(f"Your final hand: {user_list}, final score: {user_score}")
  else:
    print(f"your cards: {user_list}, current score: {user_score}")

 
  #if only one card then display that card, else add the cards
  if len(comp_list) == 1:
    print(f"Computer's first card: {comp_score}")
  else:
    if final == True:
      print(f"Computer's final hand: {comp_list}, final score: {comp_score}")
    else:
      print(f"Computer's first card: {comp_list}, current score: {comp_score}")
  return user_score, comp_score
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

play = input("Do you want to play a game of Blackjack? type 'y' or 'n': ").lower()

keep_playing = True

#keep the user's cards in here
user_card_list = []

#keep the user's cards in here
comp_card_list = []

#keep track of the user and computer scores
user_hand = 0
comp_hand = 0
final = False

if play == "y":
  #print(art.logo)
   # #first card
  draw_card(user_card_list)
  # #second card
  draw_card(user_card_list) 
  user_hand, comp_hand = scores(user_card_list, comp_card_list, user_hand, comp_hand, final)
else:
  keep_playing = False
  
while keep_playing:

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
      draw_card(user_card_list)
      user_hand, comp_hand = scores(user_card_list, comp_card_list, user_hand, comp_hand, final)
      if comp_hand > 21:
        print("You win!")
        break
      if user_hand > 21:
        print("You lose!")
        break
      # elif user_hand < 21:
      #   #draw_card(comp_card_list)
      #   if user_hand > comp_hand:
      #     print("You Win!")
      #     #break
      #   elif user_hand < 21:
      #     continue
      #   else:
      #     print("You lose!")
      #     break
      else:
        continue
    else: #another_card == 'n':
      final = True
      user_hand, comp_hand = scores(user_card_list, comp_card_list, user_hand, comp_hand, final)
      if user_hand > comp_hand:
        print("You Win!")
        break
      elif comp_hand > 21:
        print("You win!")
        break
      else:
        print("You lose!")
        break
      
