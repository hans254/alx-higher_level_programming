#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    det = list(a_dictionary.keys())[0]
    large = a_dictionary[det]
    for a, b in a_dictionary.items():
        if b > large:
            large = b
            det = a
    return (det)
