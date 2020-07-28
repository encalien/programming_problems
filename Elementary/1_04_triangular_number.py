number = int(input("Give me a number, and I'll calculate the triangular number! "))

triangular_number = 0

# i = 1
# while i <= number:
#   triangular_number += i
#   i += 1

for i in range(1, number + 1):
  triangular_number += i

print("The triangular number of", number, "is", triangular_number)

