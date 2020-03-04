import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    lower_str1 = str1.lower()
    for letter in alphabet:
        if letter not in lower_str1:
            return False
    return True
    pass


assert ispangram("The Quick Brown Fox Jumps Over The Lazy Dog")
assert not ispangram("I am not pangram")
