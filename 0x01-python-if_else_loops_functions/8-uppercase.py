#!/usr/bin/python3
def uppercase(str):
    """This Function converts the str parameter to uppercase"""
    STR = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            CHAR = chr(ord(char) - 32)
            STR += CHAR
        else:
            STR += char

    print("{}".format(STR), end="")
    print()
