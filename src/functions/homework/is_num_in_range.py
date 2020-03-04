def ran_check(num, low, high):
    # if low <= num <= high:
    if num in range(num, high + 1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('The number is outside the range.')
    pass


def ran_bool(num, low, high):
    return low <= num <= high


assert ran_bool(5, 2, 7)
