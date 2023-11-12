#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element with another in a new list.

    Args:
    - my_list: List to search and replace elements in.
    - search: Element to search for in the list.
    - replace: Element to replace occurrences of 'search' with.

    Returns:
    - New list with replacements.
    """
    # Create a new list with replaced elements
    new_list = [replace if x == search else x for x in my_list]
    return new_list

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    # Print the new list and the original list to verify that the original list is not modified
    print(new_list)
    print(my_list)
