# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    number_string = ""
    for number in nums:
        number_string = number_string + str(number)
    # print (number_string   )
    return number_string.__contains__("33")
    pass
