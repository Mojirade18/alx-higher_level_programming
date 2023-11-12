#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary.

    Args:
    - a_dictionary: Dictionary.

    Returns:
    - Number of keys in the dictionary.
    """
    # Use the len function to get the number of keys
    num_keys = len(a_dictionary.keys())

    return num_keys

# Example usage:
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
