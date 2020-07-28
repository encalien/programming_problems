import random

# define computer choses functions
def validate_guess(guess):
  if not guess:
    print("You have to guess a number between 1 and 100")
    guess_valid = False
  else:
    guess_valid = True
    for char in guess:
      if not char in "0123456789":
        print("You are allowed to type in only numbers, no letters, spaces or other characters.")
        guess_valid = False
        break
    return guess_valid

def process_guess():
  guess = input("What's your guess? ")
  guess_valid = validate_guess(guess)
  if guess_valid:
    check_guess(int(guess))
  else:
    process_guess()

def check_guess(guess):
  answer = random.randint(1, 100)
  num_of_tries = 1
  guesses = []
  while guess != answer:
    if guess in guesses:
      print("You already guessed this number.")
    else:
      guesses.append(guess)
      if guess > answer:
        print("Your number is too big!")
      else:
        print("Your number is too small!")
      num_of_tries += 1
    guess = int(input("What's your guess? "))

  print("You guessed my number in {} tries!".format(num_of_tries))

def computer_choose():
  process_guess()

# define computer guesses functions
def guess(low, high):
  new_guess = (low + high) // 2
  print("Is your number {}?".format(new_guess))
  process_reply(new_guess, low, high)

def process_reply(my_guess, low, high):
  reply = input("Y - yes, H - guess higher, L - guess lower\n")
  if not reply:
    print("You have to give me a response.")
    process_reply(my_guess, low, high)
  elif reply.casefold() == "y":
    print("Yeeey me!")
  elif reply.casefold() == "h":
    guess(my_guess + 1, high)
  elif reply.casefold() == "l":
    guess(low, my_guess - 1)
  else:
    print("I don't understand your answer.")
    process_reply(my_guess, low, high)

def computer_guess():
  guess(1, 100)

# initialize roles
def start_game():
  guessing_player = input("Who should guess this game? (C - computer, H - human)\n")
  if guessing_player.strip().casefold() == "c":
    computer_guess()
  elif guessing_player.strip().casefold() == "h":
    computer_choose()
  else:
    print("You have to pick one of us!")
    start_game()

# play the game
print("Welcome to Number Wizard!")
print("One of us has to think of a number between 1 and a 100.")
print("The other one has to guess the number, getting only the information if guess is higher or lower than the answer.")

start_game()





