# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as $$\frac{4}{3} πr^3$$
def vol(rad):
    pi = 3.14
    return (4 / 3) * pi * (rad ** 3)
    pass


assert vol(2) == 33.49333333333333
