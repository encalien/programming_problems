# 2.08    Write a function on_all that applies a function to every element of a list. Use it to print the first twenty perfect squares. The perfect squares can be found by multiplying each natural number with itself. The first few perfect squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16. Twelve for example is not a perfect square because there is no natural number m so that m*m=12. (This question is tricky if your programming language makes it difficult to pass functions as arguments.)

import math

def is_perfect_square(num):
  return True if int(math.sqrt(num)) ** 2 == num else False


def on_all(my_list):
  perfect_squares = []
  for item in my_list:
    if is_perfect_square(item):
      perfect_squares.append(item)
  return perfect_squares

my_list = [1, 5, 4, 2, 70, 54, 82, 42, 3, 12, 6, 9, 25]

print(on_all(my_list))