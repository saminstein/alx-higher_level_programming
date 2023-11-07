#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    
    if sentence:
        first_char = sentence[0]
        new_tuple = (length, first_char)
    else:
        new_tuple = (length, None)
    return new_tuple