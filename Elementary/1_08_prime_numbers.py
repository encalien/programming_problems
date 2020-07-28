# Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)

import math

# def find_primes_1(n):
#   primes = []
#   for number in range(2, n):
#     for x in range(2, math.ceil(math.sqrt(number)) + 1):
#       if number % x == 0:
#         break
#     else:
#       primes.append(number)
#   return primes

# print(find_primes_1(1_000_000))


def find_primes(max_number):
  numbers = list(range(2, max_number + 1))
  primes = []
  for i in range(max_number - 1):
    if numbers[i] != 0:
      primes.append(numbers[i])
      for j in range(1, max_number // numbers[i]):
        numbers[i + numbers[i] * j] = 0
  return primes

print(find_primes(100_000_000))