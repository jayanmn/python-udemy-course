# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an 11, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
def blackjack(a, b, c):
    # sum_of_three = a + b + c
    # if sum_of_three <= 21:
    #     return sum_of_three
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])

    # adjust
    # if a == 11 or b == 11 or c == 11:
    if 11 in [a, b, c] and sum([a, b,
                                c]) <= 31:  # this is equivalent to "If their sum exceeds 21 and there's an 11, reduce the total sum by 10."
        return sum([a, b, c]) - 10

    return "BUST"
    pass
