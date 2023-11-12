#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
    - a_dictionary: Dictionary.
    - key: Key (string).
    - value: Value (any type).

    Returns:
    - Updated dictionary.
    """
    # Update the value for the given key or add a new key-value pair
    a_dictionary[key] = value

    return a_dictionary

# Example usage:
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }

    # Test case 1: Update an existing key
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    # Test case 2: Add a new key
    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)
