def bubble_sort(my_list):
  for i in range(len(my_list)):
    for j in range(len(my_list) - 1 - i):
      if my_list[j] > my_list[j + 1]:
        temp = my_list[j + 1]
        my_list[j + 1] = my_list[j]
        my_list[j] = temp
  return my_list

def selection_sort(my_list):
  for i in range(len(my_list)):
    ind_of_lowest = i
    for j in range(i + 1, len(my_list)):
      if my_list[ind_of_lowest] > my_list[j]:
        ind_of_lowest = j
    if ind_of_lowest != i:
      temp = my_list[i]
      my_list[i] = my_list[ind_of_lowest]
      my_list[ind_of_lowest] = temp
  return my_list
