def up_low(s):
    num_up = 0
    num_low = 0
    for letter in s:
        if letter.islower():
            num_low += 1
        elif letter.isupper():
            num_up += 1
    print("No. of Upper case characters : {}".format(num_up))
    print("No. of Lower case characters : {}".format(num_low))
    pass
