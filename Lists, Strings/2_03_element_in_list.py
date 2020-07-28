def is_element_in_list(element, my_list):
  for el in my_list:
    if el == element:
      return True
  return False

my_list = [1, 5, 4, 2, 70, 54, 82, 42, 3, 12, 6]

print(is_element_in_list(42, my_list))
print(is_element_in_list(102, my_list))

# python way
# print(42 in my_list)
