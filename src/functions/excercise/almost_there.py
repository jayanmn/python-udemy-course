# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10
    # return (90 <= n <= 110) or (190 <= n <= 210)
