# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(nums):
    # index = 0
    # for num in nums:
    #     index += 1
    #     if num == 0:
    #         break
    # if index >= len(nums):
    #     return False
    #
    # # print(nums[index:])
    # for num in nums[index:]:
    #     index += 1
    #     if num == 0:
    #         break
    # if index >= len(nums):
    #     return False
    # # print(nums[index:])
    # for num in nums[index:]:
    #     index += 1
    #     if num == 7:
    #         break
    #
    # return index <= len(nums)
    spy_str = [0, 0, 7, 'x']
    for num in nums:
        if num == spy_str[0]:
            spy_str.pop(0)
    return len(spy_str) == 1  # we are left with x
    pass
