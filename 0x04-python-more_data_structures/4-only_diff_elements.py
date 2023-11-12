#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
    - set_1: First set.
    - set_2: Second set.

    Returns:
    - Set containing elements present in only one set.
    """
    # Use the symmetric_difference operation to find elements present in only one set
    diff_set = set_1.symmetric_difference(set_2)

    return diff_set

# Example usage:
if __name__ == "__main__":
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
