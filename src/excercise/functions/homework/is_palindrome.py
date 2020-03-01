def palindrome(s):
    return s == s[::-1]
    pass


assert palindrome("HelllleH")
assert not palindrome("Knife")
