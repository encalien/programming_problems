# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,...,n.

def clean_numeric_string(string):
  for char in string:
    if not char.isnumeric():
      print("You need to use the right syntax:\nTn\te.g.: 'T17'\tfor triangular number\nn!\te.g.: '17!'\tfor factorial")
      return None
  return int(string)

def calculate_triangular_number(number):
  triangular_number = 0

  for i in range(1, number + 1):
    triangular_number += i

  print("The triangular number of", number, "is", triangular_number)

def calculate_factorial(number):
  factorial = 1

  for i in range(1, number + 1):
    factorial *= i

  print("The factorial of", number, "is", factorial)

def another_query_check():
  continue_input = input("Would you like to calculate another number? Press any key to continue, or type Q anything else to quit the program.\n")
  if continue_input.casefold() != "Q".casefold():
    print("OK. Let's try another one.")
    new_query()

def new_query():
  user_input = input("What would you like me to calculate?\n")

  if "T".casefold() in user_input.casefold():
    number = clean_numeric_string(user_input[1:])
    if number:
      calculate_triangular_number(number)
      another_query_check()
    else:
      new_query()
  elif "!" in user_input:
    number = clean_numeric_string(user_input[:-1])
    if number:
      calculate_factorial(number)
      another_query_check()
    else:
      new_query()
  else:
    print("You need to define which operation you would like me to do, like so:\nTn\te.g.: 'T17'\tfor triangular number\nn!\te.g.: '17!'\tfor factorial")
    new_query()

print("Hi, there!\nI can calculate a triangular number (Tn) or a factorial (n!).")
new_query()

