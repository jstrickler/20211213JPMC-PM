#!/usr/bin/python3

spam = [ 
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM	", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]
def cleanup(s):
    # write this code ...
    return s

for string in spam:
    new_string = cleanup(string)
    print(f">{string}< >{new_string}<")
