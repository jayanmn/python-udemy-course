def multiply(numbers):
    mul = 1
    for num in numbers:
        mul *= num
    return mul
    pass


assert multiply([1, 2, 3, 4, 5]) == 120
assert multiply([1, 2, 3, 4, 5, 6]) == 720
