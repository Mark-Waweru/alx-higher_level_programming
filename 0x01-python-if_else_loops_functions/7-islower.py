#!/usr/bin/python3
def islower(c):
    """Checks if the character C is lowercase character"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
