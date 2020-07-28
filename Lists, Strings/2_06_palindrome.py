def characters_from_string(string):
  characters = ""
  for char in string.casefold():
    if char in "abcčdefghijklmnoprsštuvzžqwyx":
      characters += char
  return characters

def is_palindrome(string):
  string = characters_from_string(string)
  if string == string[::-1]:
    return True
  else:
    return False

string_1 = "Perica reže raci rep."
string_2 = "Ana"
string_3 = "Katarina"

print(is_palindrome(string_1))
print(is_palindrome(string_2))
print(is_palindrome(string_3))