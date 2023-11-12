#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
    - a_dictionary: Dictionary.
    - key: Key to delete (string).

    Returns:
    - Updated dictionary.
    """
    # Check if the key exists before deleting
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary

# Example usage:
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }

    # Test case 1: Delete an existing key
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")

    # Test case 2: Try to delete a non-existing key
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
