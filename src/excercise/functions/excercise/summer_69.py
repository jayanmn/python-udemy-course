# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    sum_of_num = 0
    ignore = False
    for num in arr:
        if num == 6:
            ignore = True
            continue
        if num == 9:
            ignore = False
            continue

        if not ignore:
            sum_of_num += num
    return sum_of_num
    pass
