#!/usr/bin/python3

def number_of_lines(filename=""):
  """
  function that returns the number of lines of a text file
  """
  with open(filename, 'r') as rf:
    lines = rf.readlines()
    number = len(lines)
    return number