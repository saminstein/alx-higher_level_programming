def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_value = 0
    best_key = None
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key
    return best_key
