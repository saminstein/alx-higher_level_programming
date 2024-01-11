#!/usr/bin/python3

def read_file(filename=""):
  """
  function that reads from a file
  
  args:
    filename: file to read from
  """
  with open(filename, 'r', encoding='utf-8') as rf:
    for line in rf:
      print(line, end='')