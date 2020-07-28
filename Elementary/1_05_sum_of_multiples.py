number = int(input("Give me a number, and I'll calculate the sum of all multiples of 3 or 5 between 1 and your number! "))

sum = 0

# i = 1
# while i <= number:
#   if (i % 3 == 0 or i % 5 == 0):
#     sum += i
#   i += 1

for i in range(1, number + 1):
  if (i % 3 == 0 or i % 5 == 0):
    sum += i

print("The sum of multiples of 3 or 5 between 1 and", number, "is", sum)

