import art

print(art.logo)

def add(n1, n2):
  return n1 + n2
  
def subtract(n1 , n2):
  return n1- n2
  
def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

proceed = True
num1 = float(input("Whats the first number? : "))
for key in operation:
   print(key)
while proceed:   
  operation_symbol = input("Pick an operation: ")
  num2 = float(input("What's the second number: "))    
  answer = operation[operation_symbol](num1, num2)  
  print(f"{num1} {operation_symbol} {num2} = {answer}")

  proceed_with_answer = True
  calc_with_prev_answer = input(f"Type 'y' to continue calculationg with {answer} or type 'n' to exit: ")
  if calc_with_prev_answer == 'n':
    break
  elif calc_with_prev_answer == 'y':
    num1 = answer
  
