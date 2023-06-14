#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (type(roman_string) == str) or roman_string is None:
        return 0
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    output, old = 0, 0
    for c in reversed(roman_string):
        value = values.get(c, 0)
        if value >= old:
            output += value
        else:
            output -= value
        old = value
    return output
