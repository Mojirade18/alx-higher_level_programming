#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
    - a_dictionary: Dictionary.

    Returns:
    - None (prints the dictionary by ordered keys).
    """
    # Sort keys alphabetically and iterate through them
    for key in sorted(a_dictionary.keys()):
        # Print each key-value pair
        print("{}: {}".format(key, a_dictionary[key]))

# Example usage:
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
