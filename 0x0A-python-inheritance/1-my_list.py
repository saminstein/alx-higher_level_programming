#!/usr/bin/python3
"""
  This module prints a list in ascending order
"""
class MyList(list):
  def print_sorted(self):
    """
    prints a list in ascending order
    sorts the list and prints it out
    """
    if issubclass(MyList, list):
      print(sorted(self))