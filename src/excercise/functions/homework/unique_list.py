def unique_list(lst):
    uniq_list = []
    for e in lst:
        if e not in uniq_list:
            uniq_list.append(e)
    return uniq_list
    pass


assert unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]) == [1, 2, 3, 4, 5]
