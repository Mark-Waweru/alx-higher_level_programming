#!/usr/bin/python3
def multiple_returns(sentence):
    """multiple_returns - returns a tuple with the length of a string
    and its first character
    @sentence: The sentence to check

    Return: The length of the string and the first character
    """
    len_first = (len(sentence), sentence[:1])
    len_firstNone = (len(sentence), None)
    if len(sentence) == 0:
        return (len_firstNone)
    else:
        return (len_first)
