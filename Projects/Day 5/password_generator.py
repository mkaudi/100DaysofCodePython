#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

print("Easy Level Password")
password = ""
for let in range(1, nr_letters + 1):
  password += str(letters[random.randint(0,len(letters) -1)])

for symb in range(1, nr_symbols + 1):
  password += str(symbols[random.randint(0,len(symbols) - 1)])
  
for num in range(1, nr_numbers + 1):
  password += str(numbers[random.randint(0,len(numbers) -1)])
  
print(f"Your password is: {str(password)}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print("Hard Level Password")
password_list = []
for let in range(1, nr_letters +1):
  password_list += str(letters[random.randint(0,len(letters) -1)])

for symb in range(1, nr_symbols + 1):
  password_list += str(symbols[random.randint(0,len(symbols) -1)])
  
for num in range(1, nr_numbers +1 ):
  password_list += str(numbers[random.randint(0,len(numbers) -1)])

random.shuffle(password_list,)

password = ""
for i in password_list:
  password += i

print(f"Your password is: {str(password)}")