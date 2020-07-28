#    ( (−1)^(k+1) ) / (2*k − 1) for each value of k from 1 to a million, multiplied by 4.

def calculate_sum():
  sum = 0
  for k in range(1, 1000000):
    sum += ( (-1) ** (k + 1) ) / (2 * k - 1)
  sum *= 4
  print(sum)

calculate_sum()