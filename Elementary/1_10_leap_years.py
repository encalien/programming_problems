def is_leap_year(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False

def print_leap_years(start_year, end_year):
  for year in range(start_year, end_year + 1):
    print("Year {} is a leap year".format(year)) if is_leap_year(year) else print("Year {} is not a leap year".format(year))

print_leap_years(1900,2200)