#!/usr/bin/python3

def write_file(filename="", text=""):
  with open(filename, mode='w', encoding='utf-8') as wf:
    wf.write(text)
    number = len(text)
    return number