#!/usr/bin/python3
from math import factorial
def pascal_triangle(n):
  result = []
  if n <= 0:
    return []
    
  for i in range(n):
    cur_row = []
    for j in range(i+1):
      if j == 0 or j == i:
        cur_row.append(1)
      else:
        current_elem = result[i-1][j-1] + result[i-1][j]
        cur_row.append(current_elem)
        
    result.append(cur_row)
    
  return result