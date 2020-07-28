# 2.10    Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

def combine_lists(list_1, list_2):
  max_common_index = len(list_1) if len(list_1) < len(list_2) else len(list_2)
  combined_list = []

  for i in range(max_common_index):
    combined_list.append(list_1[i])
    combined_list.append(list_2[i])
  return combined_list + list_1[max_common_index::] + list_2[max_common_index::]

print(combine_lists([1, 2, 3, 4, 5], ["a", "b", "c", "d", "e", "f", "g"]))