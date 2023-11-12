#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a new dictionary with only the key-value pairs
    # where the value is not equal to the specified value
    new_dict = {key: val for key, val in a_dictionary.items() if val != value}

    return new_dict
