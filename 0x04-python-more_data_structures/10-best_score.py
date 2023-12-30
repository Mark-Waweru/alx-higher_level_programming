#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    max_value = 0
    max_key = None
    for x, y in a_dictionary.items():
        if y > max_value:
            max_value = y
            max_key = x

    return(max_key)
