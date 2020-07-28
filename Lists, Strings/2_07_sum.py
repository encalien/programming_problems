# 2.07    Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion. (Subject to availability of these constructs in your language of choice.)

def for_loop_sum(my_list):
  sum = 0
  for i in my_list:
    sum += i
  return sum

def while_loop_sum(my_list):
  sum = 0
  i = 0
  while i < len(my_list):
    sum += my_list[i]
    i += 1
  return sum

def recursion_sum(my_list):
  if len(my_list) == 1:
    return my_list[0]
  else:
    return my_list.pop() + recursion_sum(my_list)

my_list = [1, 5, 4, 2, 70, 54, 82, 42, 3, 12, 6]

print(for_loop_sum(my_list))
print(while_loop_sum(my_list))
print(recursion_sum(my_list))