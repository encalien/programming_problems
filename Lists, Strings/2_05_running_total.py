def running_total(my_list):
  running_total = 0
  for element in my_list:
    running_total += element
    print("Added {}, running total is now {}".format(element, running_total))
    print("Press any key to continue.\tPress 'Q' to stop calculating and return result.")
    if input().casefold() == "q":
      break
  return running_total

my_list = [1, 5, 4, 2, 70, 54, 82, 42, 3, 12, 6]

print("The end sum is", running_total(my_list))