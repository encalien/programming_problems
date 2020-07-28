def reverse_list(my_list):
  reversed_list = []
  for i in range(len(my_list), 0, -1):
    reversed_list.append(my_list[i - 1])
  return reversed_list

def reverse_list_in_place(my_list):
  for i in range(0, len(my_list) // 2):
    temp = my_list[i]
    my_list[i] = my_list[-1 - i]
    my_list[-1 - i] = temp
  return my_list


my_list = [1, 5, 4, 2, 70, 54, 82, 42, 3, 12, 6]
print(my_list)
print(reverse_list(my_list))
print("---")
print(my_list)
print(reverse_list_in_place(my_list))
print(my_list)


# python way
# print(my_list[::-1])
# print(list(reversed(my_list)))