# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1_lower = name1.lower()
name2_lower = name2.lower()

#print(name1_lower)
#print(name2_lower)

true_count = 0
love_count = 0

true_count+=name1_lower.count("t")
true_count+=name1_lower.count("r")
true_count+=name1_lower.count("u")
true_count+=name1_lower.count("e")

true_count+=name2_lower.count("t")
true_count+=name2_lower.count("r")
true_count+=name2_lower.count("u")
true_count+=name2_lower.count("e")


love_count += name1_lower.count("l")
love_count += name1_lower.count("o")
love_count += name1_lower.count("v")
love_count += name1_lower.count("e")

love_count += name2_lower.count("l")
love_count += name2_lower.count("o")
love_count += name2_lower.count("v")
love_count += name2_lower.count("e")

#print(f"true_count {true_count}")
#print(f"love_count {love_count}")

percentage = str(true_count) + str(love_count)
perc_int = int(percentage)
#print(f"percentage {percentage}%")

if perc_int < 10 or perc_int > 90:
  print(f"Your score is {perc_int}, you go together like coke and mentos.")
elif perc_int > 40 and perc_int < 50:
  print(f"Your score is {perc_int}, you are alright together.")
else:
  print(f"Your score is {perc_int}.")
