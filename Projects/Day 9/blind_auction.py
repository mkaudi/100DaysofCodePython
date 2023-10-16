from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art

print(art.logo)
print("Welcome to the secret auction program.")
#name = input("what is your name?: ")
#bid = input("What's your bid?: ")
#more_bids = input("Are there any other bidders? Type 'yes' or 'no.\n'").lower()

another_bid = True


bids_dict = []
add_into_bids = {}
prev_bid = 0
winner = ""
index = -1
winner_index = 0
while another_bid:
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  
  add_into_bids["name"] = name
  add_into_bids["bid"] = bid
  
  bids_dict.append(add_into_bids)
  add_into_bids = {}
 
  if int(bid) > prev_bid:
    winner_index = index
    winner = bids_dict[index]["name"]
    
    
  more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if more_bids == 'yes':
    index += 1
    clear()
  else:
    another_bid = False
    clear()

#print(bids_dict)
print(f"The winner is {winner} with a bid of ${bids_dict[winner_index]['bid']}")
  