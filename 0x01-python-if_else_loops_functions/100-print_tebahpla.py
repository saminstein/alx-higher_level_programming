#!/usr/bin/python3

toggle = 0
for i in range(ord('z'), ord('a') -1, -1):
    print(chr(i - toggle), end="")
    if toggle == 0:
        toggle = 32
    else:
        toggle = 0
