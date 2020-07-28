# Write a program that prints a multiplication table for numbers up to 12.

for i in range(1, 13):
  row = "{:2}".format(i)
  for j in range(2, 13):
    row += "{:4}".format(i * j)
  print(row)
