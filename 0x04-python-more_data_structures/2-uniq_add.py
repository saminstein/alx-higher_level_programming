def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    total = 0

    for num in uniq_list:
        total += num
    return total
