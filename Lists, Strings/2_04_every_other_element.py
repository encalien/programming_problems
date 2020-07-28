def every_other_element(my_list, starting_index):
  every_other_element_list = []
  if starting_index < 0 or starting_index > 1:
    print("Starting index out of range. Must be 0 or 1.")
    return None
  print("finding odd elements") if starting_index == 1 else print("finding even elements")
  for i in range(starting_index, len(my_list), 2):
    every_other_element_list.append(my_list[i])
  return every_other_element_list

my_list = [1, 5, 4, 2, 70, 54, 82, 42, 3, 12, 6]

print(every_other_element(my_list, 1))