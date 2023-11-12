#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    Args:
    - my_list: List of integers.

    Returns:
    - Sum of all unique integers in the list.
    """
    # Use a set to store unique integers
    unique_set = set()
    
    # Add each element to the set, which automatically removes duplicates
    for num in my_list:
        unique_set.add(num)
    
    # Calculate the sum of unique integers
    result = sum(unique_set)
    
    return result

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
