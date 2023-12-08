#!/usr/bin/python3

def text_indentation(text):
  if not isinstance(text, str):
    raise TypeError("text must be a string")
  
  new_text = []
  current_text = ""
  
  for char in text:
    if char in [".", "?", ":"]:
      new_text.append(current_text.strip())
      current_text = ""
    else:
      current_text += char
      
  if current_text:
    new_text.append(current_text.strip())
    
  for text_str in  new_text:
    print(text_str)