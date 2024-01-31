def complex_delete(a_dictionary, value):
    keys_to_del = a_dictionary.copy()
    for key, val in keys_to_del.items():
        if val == value:
            del a_dictionary[key]

    return a_dictionary
