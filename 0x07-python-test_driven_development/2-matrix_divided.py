#!/usr/bin/python3
"""
This module composes of the function that divides all element of a matrix, it could be an integer or a float
"""

def matrix_divided(matrix, div):
  """
  function that divides all element in matrix
  
  parameter:
    matrix: a list of lists of (int, float)
    div: the number to divide by (int, float)
  
  Returns:
    matrix: returns the result of the divided matrix
    
  Raises:
    TypeError: Each row of the matrix must have the same size
    TypeError: div must be a number
    ZeroDivisionError: division by zero
  """
  if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
  for row in matrix:
    row_size = len(matrix[0])
    row_len = len(row)
    if row_len != row_size:
      raise TypeError("Each row of the matrix must have the same size")
      
  if not isinstance(div, (int, float)):
    raise TypeError("div must be a number")
  
  if div == 0:
    raise ZeroDivisionError("division by zero")
    
  new_mat = [[round(elem / div, 2) for elem in row] for row in matrix]
  return new_mat
  